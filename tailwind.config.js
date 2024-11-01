/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*.py", "pages/*.py"],
  theme: {
    extend: {
      animation: {
        "gradientX-top-left": "gradientX-top-left 7s ease infinite",
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
  plugins: [],
};
