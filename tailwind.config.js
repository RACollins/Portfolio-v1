/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*.py", "pages/*.py"],
  darkMode: "selector",
  theme: {
    extend: {
      colors: {
        darkblue: {
          100: "#7499ba",
          200: "#678fb4",
          300: "#5a86ad",
          400: "#507ca3",
          500: "#4a7296",
          600: "#436889",
          700: "#3d5e7c",
          800: "#37546f",
          900: "#304a61",
        },
      },
      animation: {
        "gradientX-top-left": "gradientX-top-left 17s ease infinite",
      },
      keyframes: {
        "gradientX-top-left": {
          "0%, 100%": {
            backgroundSize: "200% 200%",
            backgroundPosition: "bottom right",
          },
          "50%": {
            backgroundSize: "200% 200%",
            backgroundPosition: "top left",
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
