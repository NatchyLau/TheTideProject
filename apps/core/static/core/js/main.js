document.addEventListener("DOMContentLoaded", () => {
  // --- Navbar Scroll Logic (Same as before) ---
  const navbar = document.getElementById("navbar");
  const navContainer = navbar.querySelector(".container");
  const navBg = document.getElementById("nav-bg");
  const navTexts = document.querySelectorAll(".nav-text");
  const navCta = document.getElementById("nav-cta");
  const navCtaText = document.getElementById("nav-cta-text");
  const navDivider = document.getElementById("nav-divider");
  const logoImg = document.getElementById("logo-img");

  // Mobile Menu Elements
  const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu"); // The Drawer
  const mobileBackdrop = document.getElementById("mobile-menu-backdrop"); // The Overlay
  const mobileNavLinks = document.querySelectorAll(".mobile-nav-link");

  const updateNavbar = () => {
    const isScrolled = window.scrollY > 50;
    // Check if mobile menu is OPEN. If open, force button to be white/visible
    const isMenuOpen =
      mobileMenu && !mobileMenu.classList.contains("translate-x-full");

    if (isScrolled) {
      // --- SCROLLED STATE ---
      navbar.setAttribute("data-scrolled", "true");
      if (navContainer) navContainer.classList.replace("py-3", "py-2");

      navBg.className =
        "absolute inset-0 bg-white/95 backdrop-blur-md shadow-sm transition-all duration-500";
      navTexts.forEach((el) =>
        el.classList.replace("text-white/90", "text-premium-900"),
      );

      if (logoImg) {
        logoImg.classList.remove("brightness-0", "invert", "drop-shadow-md");
        logoImg.classList.replace("md:h-24", "md:h-20");
      }

      if (navDivider)
        navDivider.classList.replace("bg-white/30", "bg-premium-300");
      if (navCta)
        navCta.classList.replace("border-white/40", "border-premium-900");
      if (navCtaText)
        navCtaText.classList.replace("text-white", "text-premium-900");

      // Mobile Button Color Logic
      if (mobileMenuBtn) {
        if (isMenuOpen) {
          // If menu is open, button must be white (to contrast with dark drawer)
          mobileMenuBtn.classList.remove("text-premium-900");
          mobileMenuBtn.classList.add("text-white");
        } else {
          // If menu is closed and scrolled, button is dark
          mobileMenuBtn.classList.remove("text-white");
          mobileMenuBtn.classList.add("text-premium-900");
        }
      }
    } else {
      // --- TOP STATE ---
      navbar.setAttribute("data-scrolled", "false");
      if (navContainer) navContainer.classList.replace("py-2", "py-3");

      navBg.className =
        "absolute inset-0 bg-gradient-to-b from-black/50 to-transparent transition-all duration-500";
      navTexts.forEach((el) =>
        el.classList.replace("text-premium-900", "text-white/90"),
      );

      if (logoImg) {
        logoImg.classList.add("brightness-0", "invert", "drop-shadow-md");
        logoImg.classList.replace("md:h-20", "md:h-24");
      }

      if (navDivider)
        navDivider.classList.replace("bg-premium-300", "bg-white/30");
      if (navCta)
        navCta.classList.replace("border-premium-900", "border-white/40");
      if (navCtaText)
        navCtaText.classList.replace("text-premium-900", "text-white");

      if (mobileMenuBtn) {
        mobileMenuBtn.classList.remove("text-premium-900");
        mobileMenuBtn.classList.add("text-white");
      }
    }
  };

  window.addEventListener("scroll", updateNavbar, { passive: true });
  updateNavbar();

  // --- Mobile Menu Toggle Logic (Drawer) ---
  const toggleMenu = () => {
    const isClosed = mobileMenu.classList.contains("translate-x-full");

    if (isClosed) {
      // Open Menu
      mobileMenu.classList.remove("translate-x-full");

      // Show Backdrop
      mobileBackdrop.classList.remove("opacity-0", "pointer-events-none");
      mobileBackdrop.classList.add("opacity-100", "pointer-events-auto");

      // Prevent Body Scroll
      document.body.style.overflow = "hidden";

      // Ensure Button is White (because drawer is dark)
      if (mobileMenuBtn) {
        mobileMenuBtn.classList.remove("text-premium-900");
        mobileMenuBtn.classList.add("text-white");
      }
    } else {
      // Close Menu
      mobileMenu.classList.add("translate-x-full");

      // Hide Backdrop
      mobileBackdrop.classList.remove("opacity-100", "pointer-events-auto");
      mobileBackdrop.classList.add("opacity-0", "pointer-events-none");

      // Restore Body Scroll
      document.body.style.overflow = "";

      // Reset button color based on scroll position
      updateNavbar();
    }
  };

  if (mobileMenuBtn && mobileMenu && mobileBackdrop) {
    mobileMenuBtn.addEventListener("click", toggleMenu);
    mobileBackdrop.addEventListener("click", toggleMenu); // Click outside to close

    // Close menu when clicking a link
    mobileNavLinks.forEach((link) => {
      link.addEventListener("click", toggleMenu);
    });
  }

  // --- Scroll Reveal & Parallax (Unchanged) ---
  const observerOptions = { root: null, rootMargin: "0px", threshold: 0.1 };
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));

  window.addEventListener(
    "scroll",
    () => {
      const scrolled = window.scrollY;
      document.querySelectorAll(".parallax-bg").forEach((img) => {
        img.style.transform = `translateY(${scrolled * 0.4}px)`;
      });
    },
    { passive: true },
  );

  // --- Facilities Image Slider ---
  const facilitiesImg = document.getElementById("facilities-slider-img");
  if (facilitiesImg) {
    const imagesMeta = facilitiesImg.dataset.images;
    if (imagesMeta) {
      try {
        const images = JSON.parse(imagesMeta);
        let currentIndex = 0;

        if (images.length > 1) {
          setInterval(() => {
            // 1. Fade out
            facilitiesImg.style.opacity = "0";

            // 2. Wait for transition, then swap source
            setTimeout(() => {
              currentIndex = (currentIndex + 1) % images.length;
              facilitiesImg.src = images[currentIndex];

              // 3. Fade in (wait a tiny bit to ensure src is set and DOM is ready to transition back)
              requestAnimationFrame(() => {
                facilitiesImg.style.opacity = "1";
              });
            }, 500); // 500ms matches the opacity ease-in-out duration
          }, 5000); // Every 5 seconds
        }
      } catch (e) {
        console.error("Error parsing facilities images:", e);
      }
    }
  }
});
