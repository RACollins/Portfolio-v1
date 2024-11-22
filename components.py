from fasthtml.common import *
from dataclasses import dataclass
from lucide_fasthtml import Lucide


def TopBar():
    return Header(
        Div(
            Div(
                A(
                    H1(
                        "collins",
                        Span(".data", cls="text-red-500"),
                        cls="text-2xl font-bold text-darkblue-800 dark:text-gray-200",
                    ),
                    P(
                        "data scientist & analyst",
                        cls="text-sm text-darkblue-600 dark:text-gray-400",
                    ),
                    href="/",
                ),
            ),
            Nav(
                A(
                    "About",
                    href="/about",
                    cls="text-darkblue-800 dark:text-gray-200 hover:text-red-400 transition-colors",
                ),
                A(
                    "Projects",
                    href="/projects",
                    cls="text-darkblue-800 dark:text-gray-200 hover:text-red-400 transition-colors",
                ),
                A(
                    "Thoughts",
                    href="/thoughts",
                    cls="text-darkblue-800 dark:text-gray-200 hover:text-red-400 transition-colors",
                ),
                cls="flex space-x-4",
            ),
            Div(
                Button(
                    Div(
                        Div(
                            Lucide(
                                icon="moon", cls="text-darkblue-800 transition-colors"
                            ),
                            cls="absolute transform transition-all duration-300 dark:-rotate-90 dark:opacity-0",
                        ),
                        Div(
                            Lucide(icon="sun", cls="text-gray-200 transition-colors"),
                            cls="absolute transform transition-all duration-300 rotate-90 opacity-0 dark:rotate-0 dark:opacity-100",
                        ),
                        cls="flex w-5 h-5 items-center",
                    ),
                    cls="p-2 hover:bg-black hover:bg-opacity-10 dark:hover:bg-white dark:hover:bg-opacity-10 rounded-lg transition-colors",
                    onclick="toggleDarkMode()",
                ),
                cls="flex justify-end p-4",
            ),
            Img(
                src="/assets/2020-07-06.jpg?height=40&width=40",
                alt="Profile",
                width="{40}",
                height="{40}",
                cls="rounded-full",
            ),
            cls="flex justify-between items-center max-w-3xl mx-auto px-4 w-full",
        ),
        cls="mb-6 pt-6",
    )


def ChatWidget():
    return Div(
        # Chat Icon Button
        Button(
            Lucide(icon="message-circle", cls="w-6 h-6"),
            cls="fixed bottom-6 right-6 p-3 bg-red-500 hover:bg-red-600 text-white rounded-full shadow-lg transition-colors z-50",
            onclick="toggleChat()",
        ),
        # Chat Window
        Div(
            Div(
                # Chat Header
                Div(
                    H3("Chat with me", cls="text-lg font-semibold text-darkblue-800 dark:text-gray-300"),
                    Button(
                        Lucide(icon="x", cls="w-4 h-4"),
                        cls="text-darkblue-800 dark:text-gray-300 hover:text-red-500",
                        onclick="toggleChat()",
                    ),
                    cls="flex justify-between items-center p-4 border-b",
                ),
                # Chat Messages Container
                Div(
                    cls="flex-1 p-4 space-y-4 overflow-y-auto",
                    id="chat-messages",
                    style="height: 300px; scroll-behavior: smooth;",
                ),
                # Chat Input
                Form(
                    Div(
                        Input(
                            type="text",
                            placeholder="Type your message...",
                            cls="flex-1 p-2 border rounded-l-lg focus:outline-none focus:border-red-500 dark:bg-slate-800 dark:text-gray-300 dark:border-gray-700",
                            id="chat-input",
                            name="chat-input",
                            required=True,
                            # autocomplete="off",  # Prevent browser autocomplete
                        ),
                        Button(
                            "Send",
                            type="submit",
                            cls="px-4 py-2 bg-red-500 text-white rounded-r-lg hover:bg-red-600 transition-colors",
                        ),
                        cls="flex",
                    ),
                    cls="p-4 border-t dark:border-gray-700",
                    hx_post="/api/chat",
                    hx_target="#chat-messages",
                    hx_swap="beforeend",
                    _="on submit set #chat-input.value to '' then wait 10ms then call #chat-messages.scrollIntoView(false)",
                ),
                cls="flex flex-col bg-white dark:bg-slate-900 rounded-lg shadow-xl",
                style="width: 350px; height: 450px;",
            ),
            cls="fixed bottom-24 right-6 hidden",
            id="chat-window",
        ),
    )


@dataclass
class ProjectCard:
    icon: str
    title: str
    description: str
    endpoint: str

    def __ft__(self):
        return Div(
            A(
                Div(
                    Div(
                        self.icon,
                        cls="text-red-500 text-2xl mr-3 transition-colors duration-300 group-hover:text-darkblue-800 dark:group-hover:text-gray-200",
                    ),
                    H3(
                        self.title,
                        cls="text-lg font-semibold transition-colors duration-300 group-hover:text-red-500 dark:group-hover:text-gray-200",
                    ),
                    cls="flex items-center mb-2",
                ),
                P(self.description, cls="text-sm text-gray-600 dark:text-gray-400"),
                target="_blank",
                rel="noopener noreferrer",
                href=self.endpoint,  # Use the endpoint for the link
                cls="block",
            ),
            cls="project-card bg-white dark:bg-slate-900 border border-gray-200 rounded-lg p-4 mb-4 transition-all duration-300 hover:border-red-500 hover:shadow-md group",
        )
