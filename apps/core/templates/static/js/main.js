document.addEventListener("DOMContentLoaded", () => {
  // 1. Navbar Scroll Logic
  const navbar = document.getElementById("navbar");
  const navBg = document.getElementById("nav-bg");
  const navTexts = document.querySelectorAll(".nav-text");
  const logoText = document.getElementById("logo-text");
  const logoIcon = document.getElementById("logo-icon");
  const navCta = document.getElementById("nav-cta");
  const navCtaText = document.getElementById("nav-cta-text");
  const mobileBtn = document.getElementById("mobile-menu-btn");

  const updateNavbar = () => {
    if (window.scrollY > 50) {
      // Scrolled State
      navbar.setAttribute("data-scrolled", "true");
      navBg.classList.remove("bg-transparent");
      navBg.classList.add("bg-white/90", "backdrop-blur-md", "shadow-sm");

      // Text Colors -> Dark
      if(logoText) logoText.classList.replace("text-white", "text-premium-900");
      if(logoIcon) logoIcon.classList.replace("text-white", "text-accent-gold");
      if(mobileBtn) mobileBtn.classList.replace("text-white", "text-premium-900");

      navTexts.forEach((el) => {
        el.classList.replace("text-white/90", "text-premium-800");
      });

      // Button -> Solid Dark
      if(navCta) {
        navCta.classList.replace("border-white/30", "border-premium-900");
        navCta.classList.add("group-hover/btn:border-transparent");
      }
      if(navCtaText) navCtaText.classList.replace("text-white", "text-premium-900");
      
    } else {
      // Top State
      navbar.setAttribute("data-scrolled", "false");
      navBg.classList.add("bg-transparent");
      navBg.classList.remove("bg-white/90", "backdrop-blur-md", "shadow-sm");

      // Text Colors -> White
      if(logoText) logoText.classList.replace("text-premium-900", "text-white");
      if(logoIcon) logoIcon.classList.replace("text-accent-gold", "text-white");
      if(mobileBtn) mobileBtn.classList.replace("text-premium-900", "text-white");

      navTexts.forEach((el) => {
        el.classList.replace("text-premium-800", "text-white/90");
      });

      // Button -> Outline White
      if(navCta) {
        navCta.classList.replace("border-premium-900", "border-white/30");
        navCta.classList.remove("group-hover/btn:border-transparent");
      }
      if(navCtaText) navCtaText.classList.replace("text-premium-900", "text-white");
    }
  };

  window.addEventListener("scroll", updateNavbar);
  updateNavbar(); // Run on load

  // 2. Scroll Reveal
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1,
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll(".reveal").forEach((el) => {
    observer.observe(el);
  });

  // 3. Parallax Effect
  window.addEventListener("scroll", () => {
    const scrolled = window.scrollY;
    const parallaxImages = document.querySelectorAll(".parallax-bg");
    parallaxImages.forEach((img) => {
      img.style.transform = `translateY(${scrolled * 0.4}px)`;
    });
  });
});