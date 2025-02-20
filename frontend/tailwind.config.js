/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        sen: {
          light_red: '#A63D40',
          dark_red: '#852C2F',
          light_green: '#74A57F',
          dark_green: '#4B6B51',
          gray: "#536271"
        },
      }
    }
  },
  plugins: [],
}
