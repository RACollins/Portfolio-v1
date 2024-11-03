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
window.toggleDarkMode = function() {
    const newMode = !isDarkMode();
    updateDarkMode(newMode);
    // You can use this to debug
    console.log('Dark mode:', isDarkMode());
}

// Initialize dark mode based on saved preference or system preference
if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    updateDarkMode(true);
} else {
    updateDarkMode(false);
} 