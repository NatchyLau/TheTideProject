tailwind.config = {
  theme: {
    extend: {
      fontFamily: {
        sans: ["Prompt", "sans-serif"],
        serif: ["Playfair Display", "Prompt", "serif"],
      },
      colors: {
        // Minimal Luxury Palette
        premium: {
          50: "#FAFAF9", // Stone 50 (Off-white)
          100: "#F5F5F4",
          300: "#D6D3D1",
          500: "#78716C",
          800: "#292524", // Stone 800 (Charcoal)
          900: "#1C1917", // Stone 900 (Blackish)
        },
        accent: {
          gold: "#C6A87C", // Muted Gold
          gold_hover: "#B09265",
        },
      },
      letterSpacing: {
        "widest-plus": "0.15em",
      },
      transitionDuration: {
        400: "400ms",
      },
    },
  },
};
