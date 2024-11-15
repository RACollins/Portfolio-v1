function copyCode(button) {
  const code = button.parentElement.querySelector("pre code");
  if (code) {
    if (window.isSecureContext && navigator.clipboard) {
      navigator.clipboard.writeText(code.textContent);
    } else {
      const textArea = document.createElement("textarea");
      textArea.value = code.textContent;
      document.body.appendChild(textArea);
      textArea.focus({ preventScroll: true });
      textArea.select();
      try {
        document.execCommand("copy");
      } catch (err) {
        console.error("Unable to copy to clipboard", err);
      }
      document.body.removeChild(textArea);
    }
    button.innerHTML = `<svg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><rect width='8' height='4' x='8' y='2' rx='1' ry='1'/><path d='M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2'/><path d='m9 14 2 2 4-4'/></svg>`;
    setTimeout(() => {
      button.innerHTML = `<svg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><rect width='8' height='4' x='8' y='2' rx='1' ry='1'/><path d='M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2'/><path d='M12 11v6'/><path d='M9 14h6'/></svg>`;
    }, 1000);
  }
}
