// Function to check dark mode status
function isDarkMode() {
    return document.documentElement.classList.contains('dark');
}

// Function to update dark mode
function updateDarkMode(isDark) {
    if (isDark) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
    localStorage.theme = isDark ? 'dark' : 'light';
}

// Function to toggle dark mode
function toggleDarkMode() {
    const newMode = !isDarkMode();
    updateDarkMode(newMode);
}

// Initialize dark mode based on saved preference or system preference
function initializeDarkMode() {
    // Check if there's a saved preference
    if (localStorage.theme === 'dark' || localStorage.theme === 'light') {
        updateDarkMode(localStorage.theme === 'dark');
    } else {
        // If no saved preference, use system preference
        updateDarkMode(window.matchMedia('(prefers-color-scheme: dark)').matches);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', initializeDarkMode);

// Update the TopBar button onclick handler 