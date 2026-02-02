document.addEventListener("DOMContentLoaded", () => {
  // 1. Navbar Elements
  const navbar = document.getElementById("navbar");
  const navContainer = navbar.querySelector(".container");
  const navBg = document.getElementById("nav-bg");
  const navTexts = document.querySelectorAll(".nav-text");
  const navCta = document.getElementById("nav-cta");
  const navCtaText = document.getElementById("nav-cta-text");
  const navDivider = document.getElementById("nav-divider");
  const logoImg = document.getElementById("logo-img");
  
  // เพิ่ม: Element ปุ่ม Line
  const navLine = document.getElementById("nav-line");

  // Mobile Menu Elements
  const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");
  const mobileBackdrop = document.getElementById("mobile-menu-backdrop");
  const mobileNavLinks = document.querySelectorAll(".mobile-nav-link");

  const updateNavbar = () => {
    const isScrolled = window.scrollY > 50;
    const isMenuOpen = mobileMenu && !mobileMenu.classList.contains("translate-x-full");

    if (isScrolled) {
      // --- SCROLLED STATE (White Background) ---
      navbar.setAttribute("data-scrolled", "true");
      if (navContainer) navContainer.classList.replace("py-3", "py-2");

      navBg.className = "absolute inset-0 bg-white/95 backdrop-blur-md shadow-sm transition-all duration-500";
      
      navTexts.forEach((el) => {
        el.classList.replace("text-white/90", "text-premium-900");
      });

      if (logoImg) {
        logoImg.classList.remove("brightness-0", "invert", "drop-shadow-md");
        logoImg.classList.replace("md:h-24", "md:h-20");
      }

      if (navDivider) navDivider.classList.replace("bg-white/30", "bg-premium-300");
      
      // Update Appointment Button
      if (navCta) navCta.classList.replace("border-white/40", "border-premium-900");
      if (navCtaText) navCtaText.classList.replace("text-white", "text-premium-900");

      // --- เพิ่ม: Update Line Button (Dark Mode) ---
      if (navLine) {
         // เปลี่ยนขอบเป็นสีเข้ม
         navLine.classList.replace("border-white/40", "border-premium-900");
         // เปลี่ยนไอคอนข้างในเป็นสีเข้ม (เพื่อให้มองเห็นบนพื้นขาว)
         const lineIcon = navLine.querySelector("svg");
         if(lineIcon) lineIcon.classList.replace("text-white", "text-premium-900");
      }

      // Mobile Menu Button
      if (mobileMenuBtn) {
        if (isMenuOpen) {
          mobileMenuBtn.classList.remove("text-premium-900");
          mobileMenuBtn.classList.add("text-white");
        } else {
          mobileMenuBtn.classList.remove("text-white");
          mobileMenuBtn.classList.add("text-premium-900");
        }
      }

    } else {
      // --- TOP STATE (Transparent Background) ---
      navbar.setAttribute("data-scrolled", "false");
      if (navContainer) navContainer.classList.replace("py-2", "py-3");

      navBg.className = "absolute inset-0 bg-gradient-to-b from-black/50 to-transparent transition-all duration-500";
      
      navTexts.forEach((el) => {
        el.classList.replace("text-premium-900", "text-white/90");
      });

      if (logoImg) {
        logoImg.classList.add("brightness-0", "invert", "drop-shadow-md");
        logoImg.classList.replace("md:h-20", "md:h-24");
      }

      if (navDivider) navDivider.classList.replace("bg-premium-300", "bg-white/30");
      
      // Update Appointment Button
      if (navCta) navCta.classList.replace("border-premium-900", "border-white/40");
      if (navCtaText) navCtaText.classList.replace("text-premium-900", "text-white");

      // --- เพิ่ม: Update Line Button (Light Mode) ---
      if (navLine) {
         // เปลี่ยนขอบกลับเป็นสีขาว
         navLine.classList.replace("border-premium-900", "border-white/40");
         // เปลี่ยนไอคอนกลับเป็นสีขาว
         const lineIcon = navLine.querySelector("svg");
         if(lineIcon) lineIcon.classList.replace("text-premium-900", "text-white");
      }

      if (mobileMenuBtn) {
        mobileMenuBtn.classList.remove("text-premium-900");
        mobileMenuBtn.classList.add("text-white");
      }
    }
  };

  window.addEventListener("scroll", updateNavbar, { passive: true });
  updateNavbar();

  // 2. Mobile Menu Logic
  const toggleMenu = () => {
    const isClosed = mobileMenu.classList.contains("translate-x-full");

    if (isClosed) {
      mobileMenu.classList.remove("translate-x-full");
      mobileBackdrop.classList.remove("opacity-0", "pointer-events-none");
      mobileBackdrop.classList.add("opacity-100", "pointer-events-auto");
      document.body.style.overflow = "hidden";
      
      // Force button white when drawer is open
      if (mobileMenuBtn) {
        mobileMenuBtn.classList.remove("text-premium-900");
        mobileMenuBtn.classList.add("text-white");
      }
    } else {
      mobileMenu.classList.add("translate-x-full");
      mobileBackdrop.classList.remove("opacity-100", "pointer-events-auto");
      mobileBackdrop.classList.add("opacity-0", "pointer-events-none");
      document.body.style.overflow = "";
      
      updateNavbar(); // Reset colors
    }
  };

  if (mobileMenuBtn && mobileMenu && mobileBackdrop) {
    mobileMenuBtn.addEventListener("click", toggleMenu);
    mobileBackdrop.addEventListener("click", toggleMenu);
    document.querySelectorAll(".mobile-nav-link").forEach((link) => {
      link.addEventListener("click", toggleMenu);
    });
  }

  // 3. Scroll Reveal & Parallax
  const observerOptions = { root: null, rootMargin: "0px", threshold: 0.1 };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));

  window.addEventListener("scroll", () => {
      const scrolled = window.scrollY;
      document.querySelectorAll(".parallax-bg").forEach((img) => {
        img.style.transform = `translateY(${scrolled * 0.4}px)`;
      });
  }, { passive: true });

  // 4. Facilities Slider Logic (ถ้ามี)
  const facilitiesImg = document.getElementById("facilities-slider-img");
  // ... (ส่วน Slider เดิมของคุณ)
  if (facilitiesImg) {
    const imagesMeta = facilitiesImg.dataset.images;
    if (imagesMeta) {
      try {
        const images = JSON.parse(imagesMeta);
        let currentIndex = 0;
        if (images.length > 1) {
          setInterval(() => {
            facilitiesImg.style.opacity = "0";
            setTimeout(() => {
              currentIndex = (currentIndex + 1) % images.length;
              facilitiesImg.src = images[currentIndex];
              requestAnimationFrame(() => {
                facilitiesImg.style.opacity = "1";
              });
            }, 500);
          }, 5000);
        }
      } catch (e) {}
    }
  }
});