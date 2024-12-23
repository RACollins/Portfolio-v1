from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple
import os
from pathlib import Path
import frontmatter
import markdown
from bs4 import BeautifulSoup
import re
import numpy as np
from sentence_transformers import SentenceTransformer
# import nltk   # <--- not needed yet
# from nltk.tokenize import sent_tokenize  # <--- not needed yet
import faiss
import json

# Set tokenizers parallelism before importing/using any models
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Download required NLTK data
""" try:
    nltk.data.find("punkt_tab")
except LookupError:
    nltk.download("punkt_tab") """  # <--- not needed yet

abs_base_path = os.path.dirname(os.path.abspath(__file__))

@dataclass
class Document:
    """Represents a chunk of text with its metadata."""

    content: str
    metadata: Dict[str, str]
    embeddings: Optional[np.ndarray] = None
    id: Optional[int] = None  # Added for FAISS indexing


@dataclass
class RagConfig:
    # Paths for different document types
    cv_path: str = abs_base_path + "/../cv"
    thoughts_path: str = abs_base_path + "/../thoughts"

    # Enhanced chunking configuration
    chunk_size: int = 500
    chunk_overlap: int = 50
    min_chunk_size: int = 100  # Minimum size for a valid chunk

    # Enhanced vector store configuration
    vector_store_path: str = abs_base_path + "/../vector_store"
    index_file: str = "faiss.index"
    metadata_file: str = "metadata.json"
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_dim: int = 384  # Dimension for all-MiniLM-L6-v2

    # Search configuration
    top_k: int = 3
    similarity_threshold: float = 0.4

    # File patterns to include/exclude
    include_patterns: List[str] = ("*.md", "*.txt")
    exclude_patterns: List[str] = (
        "__pycache__",
        "*.py",
        "*.pyc",
        ".git",
        "*.ipynb",
        "*.ipynb_checkpoints",
    )


class RagService:
    def __init__(self, config: Optional[RagConfig] = None):
        self.config = config or RagConfig()
        self.documents: Dict[str, str] = {}
        self.chunks: List[Document] = []
        self.embedding_model = SentenceTransformer(self.config.embedding_model)

        # Initialize FAISS index
        self.index = faiss.IndexFlatL2(self.config.embedding_dim)
        self.next_id = 0

        # Create vector store directory if it doesn't exist
        os.makedirs(self.config.vector_store_path, exist_ok=True)

        # Try to load existing index
        self._load_vector_store()

    def load_markdown(self, file_path: Path) -> str:
        """Load and parse markdown files (CV and thoughts)."""
        try:
            # Parse frontmatter and content
            post = frontmatter.load(file_path)
            metadata = dict(post.metadata)
            content = post.content

            # Convert markdown to text
            html = markdown.markdown(content)
            soup = BeautifulSoup(html, "html.parser")
            text = soup.get_text(separator=" ", strip=True)

            # Combine metadata and content
            metadata_text = " ".join(f"{k}: {v}" for k, v in metadata.items())
            return f"{metadata_text}\n\n{text}"

        except Exception as e:
            print(f"Error loading markdown file {file_path}: {e}")
            return ""

    def load_text(self, file_path: Path) -> str:
        """Load and parse text files."""
        try:
            # Read the text file
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Create basic metadata
            metadata = {
                "filename": file_path.name,
                "type": "text",
            }

            # Combine metadata and content
            metadata_text = " ".join(f"{k}: {v}" for k, v in metadata.items())
            return f"{metadata_text}\n\n{text}"

        except Exception as e:
            print(f"Error loading text file {file_path}: {e}")
            return ""

    def should_process_file(self, file_path: Path) -> bool:
        """Check if file should be processed based on include/exclude patterns."""
        # Check exclude patterns first
        for pattern in self.config.exclude_patterns:
            if file_path.match(pattern):
                return False

        # Then check include patterns
        for pattern in self.config.include_patterns:
            if file_path.match(pattern):
                return True

        return False

    def load_docs(self) -> Dict[str, str]:
        """Load all documents from configured paths."""
        paths_to_scan = [
            Path(self.config.cv_path),
            Path(self.config.thoughts_path),
        ]

        for base_path in paths_to_scan:
            print(base_path)
            if not base_path.exists():
                print(f"Warning: Path {base_path} does not exist")
                continue

            for file_path in base_path.rglob("*"):
                if not self.should_process_file(file_path):
                    continue

                if file_path.suffix == ".md":
                    self.documents[str(file_path)] = self.load_markdown(file_path)
                elif file_path.suffix == ".txt":
                    self.documents[str(file_path)] = self.load_text(file_path)

        return self.documents

    def create_chunks(self, text: str, metadata: Dict[str, str]) -> List[Document]:
        """Split text into overlapping chunks."""
        try:
            # Try sentence tokenization first
            sentences = sent_tokenize(text)
        except Exception as e:
            print(
                f"Warning: Sentence tokenization failed, falling back to simple splitting: {e}"
            )
            # Simple fallback: split on periods, exclamation marks, and question marks
            sentences = [s.strip() for s in re.split("[.!?]", text) if s.strip()]

        chunks = []
        current_chunk = []
        current_size = 0

        for sentence in sentences:
            sentence_size = len(sentence)

            # If adding this sentence would exceed chunk_size,
            # store current chunk and start new one
            if (
                current_size + sentence_size > self.config.chunk_size
                and current_size > self.config.min_chunk_size
            ):
                # Create chunk with overlap
                chunk_text = " ".join(current_chunk)
                chunks.append(Document(content=chunk_text, metadata=metadata.copy()))

                # Keep last few sentences for overlap
                overlap_size = 0
                overlap_sentences = []
                for sent in reversed(current_chunk):
                    if overlap_size + len(sent) > self.config.chunk_overlap:
                        break
                    overlap_sentences.insert(0, sent)
                    overlap_size += len(sent)

                current_chunk = overlap_sentences
                current_size = overlap_size

            current_chunk.append(sentence)
            current_size += sentence_size

        # Don't forget the last chunk
        if current_chunk and current_size > self.config.min_chunk_size:
            chunks.append(
                Document(content=" ".join(current_chunk), metadata=metadata.copy())
            )

        return chunks

    def parse_docs(self) -> List[Document]:
        """Parse loaded documents into chunks and compute embeddings."""
        if not self.documents:
            self.load_docs()

        self.chunks = []
        for file_path, content in self.documents.items():
            metadata = {
                "source": str(file_path),
                "type": "markdown" if file_path.endswith(".md") else "txt",
            }

            # Create chunks for this document
            doc_chunks = self.create_chunks(content, metadata)
            self.chunks.extend(doc_chunks)

        # Compute embeddings for all chunks
        self._compute_embeddings()

        return self.chunks

    def _compute_embeddings(self):
        """Compute embeddings for all chunks and add to FAISS index."""
        if not self.chunks:
            return

        # Process chunks in batches to avoid memory issues
        batch_size = 32
        for i in range(0, len(self.chunks), batch_size):
            batch = self.chunks[i : i + batch_size]
            texts = [chunk.content for chunk in batch]
            embeddings = self.embedding_model.encode(texts)

            # Store embeddings and add to FAISS index
            for chunk, embedding in zip(batch, embeddings):
                chunk.embeddings = embedding
                chunk.id = self.next_id
                self.index.add(np.array([embedding], dtype=np.float32))
                self.next_id += 1

        # Save updated index
        self._save_vector_store()

    def _save_vector_store(self):
        """Save FAISS index and metadata to disk."""
        index_path = Path(self.config.vector_store_path) / self.config.index_file
        metadata_path = Path(self.config.vector_store_path) / self.config.metadata_file

        # Save FAISS index
        faiss.write_index(self.index, str(index_path))

        # Save metadata
        metadata = {
            str(chunk.id): {"content": chunk.content, "metadata": chunk.metadata}
            for chunk in self.chunks
            if chunk.id is not None
        }

        with open(metadata_path, "w") as f:
            json.dump(metadata, f)

    def _load_vector_store(self):
        """Load FAISS index and metadata from disk."""
        index_path = Path(self.config.vector_store_path) / self.config.index_file
        metadata_path = Path(self.config.vector_store_path) / self.config.metadata_file

        if not (index_path.exists() and metadata_path.exists()):
            return

        try:
            # Load FAISS index
            self.index = faiss.read_index(str(index_path))

            # Load metadata
            with open(metadata_path, "r") as f:
                metadata = json.load(f)

            # Reconstruct chunks
            self.chunks = []
            for chunk_id, data in metadata.items():
                chunk = Document(
                    content=data["content"], metadata=data["metadata"], id=int(chunk_id)
                )
                self.chunks.append(chunk)

            self.next_id = max(int(id) for id in metadata.keys()) + 1

        except Exception as e:
            print(f"Error loading vector store: {e}")
            # Initialize new index if loading fails
            self.index = faiss.IndexFlatL2(self.config.embedding_dim)
            self.next_id = 0

    def get_relevant_context(self, query: str) -> str:
        """Get relevant context for a given query."""
        # Encode query
        query_embedding = self.embedding_model.encode([query])[0]

        # Search in FAISS index
        distances, indices = self.index.search(
            np.array([query_embedding], dtype=np.float32), self.config.top_k
        )

        # Filter by similarity threshold and sort by relevance
        relevant_chunks = []
        for dist, idx in zip(distances[0], indices[0]):
            # Convert L2 distance to similarity score (inverse relationship)
            similarity = 1 / (1 + dist)
            if similarity >= self.config.similarity_threshold:
                chunk = next((c for c in self.chunks if c.id == idx), None)
                if chunk:
                    relevant_chunks.append((chunk, similarity))

        # Sort by similarity
        relevant_chunks.sort(key=lambda x: x[1], reverse=True)

        # Format context string
        if not relevant_chunks:
            return ""

        context_parts = []
        for chunk, similarity in relevant_chunks:
            source = chunk.metadata.get("source", "unknown")
            context_parts.append(
                f"[Source: {source}] (Similarity: {similarity:.2f})\n{chunk.content}"
            )

        return "\n\n".join(context_parts)
