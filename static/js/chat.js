function toggleChat() {
  const chatWindow = document.getElementById("chat-window");
  if (chatWindow.classList.contains("hidden")) {
    chatWindow.classList.remove("hidden");
    // Focus the input when opening
    document.getElementById("chat-input").focus();
  } else {
    chatWindow.classList.add("hidden");
  }
}
