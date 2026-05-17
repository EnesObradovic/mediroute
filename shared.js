/* ============================================
   MediRoute — Shared JavaScript
   Mobile menu, Dark mode, Scroll animations, 
   Language switcher, Settings dropdown
   ============================================ */

(function() {
  'use strict';

  // ── Inject Mobile Menu + Overlay into DOM ──
  function injectMobileMenu() {
    // Overlay
    const overlay = document.createElement('div');
    overlay.className = 'mobile-menu-overlay';
    overlay.id = 'mobile-overlay';
    overlay.addEventListener('click', closeMobileMenu);
    document.body.appendChild(overlay);

    // Menu drawer
    const menu = document.createElement('div');
    menu.className = 'mobile-menu';
    menu.id = 'mobile-menu';
    menu.innerHTML = `
      <div class="flex items-center justify-between mb-6">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-white rounded-lg flex items-center justify-center shadow">
            <i class="fa-solid fa-heart-pulse text-navy-800 text-base"></i>
          </div>
          <span class="text-white font-bold text-lg">Medi<span class="text-blue-300">Route</span></span>
        </div>
        <button onclick="closeMobileMenu()" class="w-8 h-8 flex items-center justify-center rounded-lg bg-white/10 text-white hover:bg-white/20 transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <a href="/" data-i18n="nav_home"><i class="fa-solid fa-magnifying-glass w-5 text-center text-sm"></i> Home</a>
      
      <div class="menu-divider"></div>
      <a href="/treatments" class="block text-blue-500 text-[10px] font-bold uppercase tracking-widest px-4 mb-2 mt-2" data-i18n="footer_treatments">Treatments</a>
      <a href="/treatment/hair-transplant" style="padding-left:2rem;font-size:13px;" data-i18n="treat_hair"><i class="fa-solid fa-scissors w-5 text-center text-xs opacity-70"></i> Hair Transplant</a>
      <a href="/treatment/dental" style="padding-left:2rem;font-size:13px;" data-i18n="treat_dental"><i class="fa-solid fa-tooth w-5 text-center text-xs opacity-70"></i> Dental</a>
      <a href="/treatment/aesthetics" style="padding-left:2rem;font-size:13px;" data-i18n="treat_aesthetics"><i class="fa-solid fa-face-smile w-5 text-center text-xs opacity-70"></i> Aesthetics</a>
      <a href="/treatment/bariatric" style="padding-left:2rem;font-size:13px;" data-i18n="treat_bariatric"><i class="fa-solid fa-weight-scale w-5 text-center text-xs opacity-70"></i> Bariatric</a>
      <a href="/treatment/eye-surgery" style="padding-left:2rem;font-size:13px;" data-i18n="treat_eye"><i class="fa-solid fa-eye w-5 text-center text-xs opacity-70"></i> Eye Laser</a>
      <div class="menu-divider"></div>

      <a href="/compare" data-i18n="nav_compare"><i class="fa-solid fa-table-columns w-5 text-center text-sm"></i> Compare Clinics</a>
      <a href="/about" data-i18n="nav_about"><i class="fa-solid fa-building w-5 text-center text-sm"></i> About Us</a>
      <a href="/blog" data-i18n="nav_blog"><i class="fa-solid fa-book-open w-5 text-center text-sm"></i> Guides / Blog</a>
      <a href="/faq" data-i18n="nav_faq"><i class="fa-solid fa-circle-question w-5 text-center text-sm"></i> FAQ</a>
      <a href="/contact" data-i18n="nav_contact"><i class="fa-solid fa-envelope w-5 text-center text-sm"></i> Contact</a>
      <div class="menu-divider"></div>
      <a href="/clinic-dashboard" data-i18n="nav_clinics"><i class="fa-solid fa-hospital w-5 text-center text-sm"></i> For Clinics</a>
      <a href="/patient-dashboard" data-i18n="nav_dashboard"><i class="fa-solid fa-gauge-high w-5 text-center text-sm"></i> My Dashboard</a>
      <div class="menu-divider"></div>
      <a href="/auth" class="!bg-emerald-600 !text-white !font-bold mt-2 justify-center" data-i18n="nav_signin"><i class="fa-solid fa-right-to-bracket w-5 text-center text-sm"></i> Sign In / Register</a>
      
      <!-- Mobile Language Selector -->
      <div class="menu-divider"></div>
      <p class="text-blue-500 text-[10px] font-bold uppercase tracking-widest px-4 mb-2 mt-2" data-i18n="nav_language">Language</p>
      <div id="mobile-lang-list" class="flex flex-col gap-1">
        <!-- Filled by JS -->
      </div>
    `;
    document.body.appendChild(menu);
  }

  // ── Mobile Menu Open/Close ──
  window.openMobileMenu = function() {
    document.getElementById('mobile-menu').classList.add('open');
    document.getElementById('mobile-overlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  window.closeMobileMenu = function() {
    document.getElementById('mobile-menu').classList.remove('open');
    document.getElementById('mobile-overlay').classList.remove('open');
    document.body.style.overflow = '';
  };

  // ── Dark Mode ──
  function initDarkMode() {
    const saved = localStorage.getItem('mediroute-dark');
    if (saved === 'true') {
      document.documentElement.classList.add('dark');
    }
  }

  window.toggleDarkMode = function() {
    document.documentElement.classList.toggle('dark');
    const isDark = document.documentElement.classList.contains('dark');
    localStorage.setItem('mediroute-dark', isDark);
    // Update toggle icons
    document.querySelectorAll('.dark-mode-icon').forEach(el => {
      el.className = isDark 
        ? 'fa-solid fa-sun dark-mode-icon' 
        : 'fa-solid fa-moon dark-mode-icon';
    });
  };

  // ── Settings Dropdown ──
  window.toggleSettings = function(e) {
    e && e.stopPropagation();
    const dd = document.getElementById('settings-dropdown');
    if (dd) dd.classList.toggle('open');
    // Close lang dropdown if open
    const ld = document.getElementById('lang-dropdown');
    if (ld) ld.classList.remove('open');
  };

  // ── Language Dropdown ──
  window.toggleLangDropdown = function(e) {
    e && e.stopPropagation();
    const dd = document.getElementById('lang-dropdown');
    if (dd) dd.classList.toggle('open');
    // Close settings dropdown if open
    const sd = document.getElementById('settings-dropdown');
    if (sd) sd.classList.remove('open');
  };

  // Close dropdowns on outside click
  document.addEventListener('click', function(e) {
    const sd = document.getElementById('settings-dropdown');
    const ld = document.getElementById('lang-dropdown');
    if (sd && !e.target.closest('.settings-dropdown-wrapper')) sd.classList.remove('open');
    if (ld && !e.target.closest('.lang-dropdown-wrapper')) ld.classList.remove('open');
  });

  // ── Scroll Animations (IntersectionObserver) ──
  function initScrollAnimations() {
    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('animated');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.animate-on-scroll').forEach(function(el) {
      observer.observe(el);
    });
  }

  // ── Language Switcher ──
  const LANGUAGES = [
    { code: 'en', flag: '🇬🇧', name: 'English',   nativeName: 'English' },
    { code: 'tr', flag: '🇹🇷', name: 'Türkçe',    nativeName: 'Türkçe' },
    { code: 'ar', flag: '🇸🇦', name: 'العربية',    nativeName: 'العربية' },
    { code: 'de', flag: '🇩🇪', name: 'Deutsch',   nativeName: 'Deutsch' },
    { code: 'fr', flag: '🇫🇷', name: 'Français',  nativeName: 'Français' },
  ];

  function getCurrentLang() {
    // Check URL param first, then localStorage, default to 'en'
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    if (urlLang && LANGUAGES.find(l => l.code === urlLang)) return urlLang;
    return localStorage.getItem('mediroute-lang') || 'en';
  }

  function buildLangDropdown() {
    const currentLang = getCurrentLang();
    const currentLangObj = LANGUAGES.find(l => l.code === currentLang) || LANGUAGES[0];

    // Desktop dropdown menu items
    const dd = document.getElementById('lang-dropdown');
    if (dd) {
      dd.innerHTML = LANGUAGES.map(l => `
        <a href="javascript:void(0)" onclick="switchLanguage('${l.code}')" class="${l.code === currentLang ? 'active' : ''}">
          <span class="flag-emoji">${l.flag}</span>
          <span class="lang-name">${l.nativeName}</span>
          <i class="fa-solid fa-check lang-check"></i>
        </a>
      `).join('');
    }

    // Update button text
    const btn = document.getElementById('lang-btn-text');
    if (btn) btn.textContent = currentLangObj.flag + ' ' + currentLangObj.code.toUpperCase();

    // Mobile language list
    const mobileLangList = document.getElementById('mobile-lang-list');
    if (mobileLangList) {
      mobileLangList.innerHTML = LANGUAGES.map(l => `
        <a href="javascript:void(0)" onclick="switchLanguage('${l.code}')" class="${l.code === currentLang ? '!bg-white/15 !text-white' : ''}">
          <span style="font-size:1.1rem">${l.flag}</span> ${l.nativeName}
          ${l.code === currentLang ? '<i class="fa-solid fa-check text-emerald-400 text-xs ml-auto"></i>' : ''}
        </a>
      `).join('');
    }
  }

  window.switchLanguage = async function(lang) {
    localStorage.setItem('mediroute-lang', lang);
    
    // Update URL param without reload for SPA feel
    const url = new URL(window.location);
    url.searchParams.set('lang', lang);
    window.history.replaceState({}, '', url);

    // Apply translations to data-i18n elements
    applyTranslations(lang);

    // Update HTML lang attribute & direction
    document.documentElement.lang = lang;
    if (lang === 'ar') {
      document.documentElement.dir = 'rtl';
    } else {
      document.documentElement.dir = 'ltr';
    }

    // Update hreflang meta tags
    updateHreflangTags(lang);

    // Fire page-specific language hook IMMEDIATELY (before any async ops)
    if (typeof window.onLanguageChanged === "function") {
      try { window.onLanguageChanged(lang); } catch(e) { console.warn('onLanguageChanged error:', e); }
    }

    // Rebuild dropdown to show new active state
    buildLangDropdown();

    // Close dropdowns
    const dd = document.getElementById('lang-dropdown');
    if (dd) dd.classList.remove('open');
    closeMobileMenu();

    // Async operations that should not block UI
    try {
      await updateNavbarSession();
    } catch(e) { console.warn('Session update error:', e); }

    // Re-render clinic cards if on index page
    try {
      if (typeof renderAllClinics === 'function' && document.getElementById('clinic-list')) {
        var treatSel = document.getElementById('treatment-select');
        var citySel = document.getElementById('city-select');
        var ratingEl = document.querySelector('input[name="rating"]:checked');
        var priceEl = document.getElementById('price-range');
        var jciEl = document.getElementById('f-jci');
        await renderAllClinics('clinic-list', {
          treatment: treatSel ? treatSel.value : '',
          city: citySel ? citySel.value : '',
          minRating: ratingEl ? parseFloat(ratingEl.value) : 0,
          maxPrice: priceEl ? parseInt(priceEl.value) : 15000,
          jci: jciEl && jciEl.checked
        });
      }
    } catch(e) { console.warn('Clinic render error:', e); }
  };

  function applyTranslations(lang) {
    if (typeof window.MEDIROUTE_I18N === 'undefined') return;
    const dict = window.MEDIROUTE_I18N[lang];
    if (!dict) return;

    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      const key = el.getAttribute('data-i18n');
      if (dict[key] !== undefined) {
        // Check if it's an input placeholder
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          el.placeholder = dict[key];
        } else if (el.tagName === 'OPTION') {
          el.textContent = dict[key];
        } else {
          el.innerHTML = dict[key];
        }
      }
    });

    // Update page title & meta description (SEO module handles this if loaded)
    if (typeof window.__MR_SEO_UPDATE === 'function') {
      window.__MR_SEO_UPDATE(lang);
    } else {
      if (dict['page_title']) document.title = dict['page_title'];
      const metaDesc = document.querySelector('meta[name="description"]');
      if (metaDesc && dict['page_description']) {
        metaDesc.setAttribute('content', dict['page_description']);
      }
    }
  }

  function updateHreflangTags(currentLang) {
    // Remove existing hreflang tags
    document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(el => el.remove());

    const baseUrl = window.location.origin + window.location.pathname;
    LANGUAGES.forEach(function(l) {
      const link = document.createElement('link');
      link.rel = 'alternate';
      link.hreflang = l.code;
      link.href = baseUrl + '?lang=' + l.code;
      document.head.appendChild(link);
    });

    // x-default
    const xdef = document.createElement('link');
    xdef.rel = 'alternate';
    xdef.hreflang = 'x-default';
    xdef.href = baseUrl + '?lang=en';
    document.head.appendChild(xdef);
  }

  // ── Highlight active nav link ──
  function highlightActiveNav() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('nav a, .mobile-menu a').forEach(function(link) {
      const href = link.getAttribute('href');
      if (href === currentPage) {
        link.classList.add('text-white', 'font-semibold');
      }
    });
  }

  // ── Navbar Session Awareness ──
  async function updateNavbarSession() {
    var session = null;

    // Try Supabase first, fallback to localStorage
    if (window.MR && MR.supabase && MR.supabase.getSimpleSession) {
      try { session = await MR.supabase.getSimpleSession(); } catch(e) {}
    }
    if (!session) {
      try { session = JSON.parse(localStorage.getItem('mr_session')); } catch(e) {}
    }
    if (!session || !session.loggedIn) return;

    // Determine destination URL
    var destUrl = 'patient-dashboard.html';
    var dashText = 'Dashboard';
    if (session.email && session.email.toLowerCase().includes('admin')) {
      destUrl = 'admin.html';
      dashText = 'Admin Panel';
    } else if (session.email && session.email.toLowerCase().includes('clinic')) {
      destUrl = 'provider.html';
      dashText = 'Clinic Panel';
    }

    // Find "Sign In" link in navbar
    var signinLinks = document.querySelectorAll('a[data-i18n="cta_signin"]');
    signinLinks.forEach(function(link) {
      var name = session.name || 'User';
      var initial = name[0] || 'U';
      link.href = destUrl;
      link.innerHTML = '<div style="display:flex;align-items:center;gap:6px;">' +
        '<div style="width:26px;height:26px;border-radius:8px;background:linear-gradient(135deg,#3B5FDD,#5C7EFF);display:flex;align-items:center;justify-content:center;color:#fff;font-size:.7rem;font-weight:700;">' + initial + '</div>' +
        '<span style="color:#fff;font-weight:600;">' + name.split(' ')[0] + '</span></div>';
    });

    // Update mobile menu Sign In link
    var mobileSignin = document.querySelector('.mobile-menu a[data-i18n="nav_signin"]');
    if (mobileSignin) {
      mobileSignin.href = destUrl;
      mobileSignin.innerHTML = '<i class="fa-solid fa-gauge-high w-5 text-center text-sm"></i> ' + dashText;
      // Add logout link
      var logoutLink = document.createElement('a');
      logoutLink.href = 'javascript:void(0)';
      logoutLink.onclick = async function() {
        if (window.MR && MR.supabase) await MR.supabase.signOut();
        localStorage.removeItem('mr_session');
        window.location.href = '/auth';
      };
      logoutLink.className = mobileSignin.className.replace('!bg-emerald-600', '!bg-red-600');
      logoutLink.innerHTML = '<i class="fa-solid fa-right-from-bracket w-5 text-center text-sm"></i> Sign Out';
      mobileSignin.parentNode.insertBefore(logoutLink, mobileSignin.nextSibling);
    }
  }

  // ── Auto-load quote-modal.js on pages that don't have it ──
  function autoLoadQuoteModal() {
    // Skip admin/auth/dashboard pages
    var skip = ['admin.html', 'auth.html', 'patient-dashboard.html', 'clinic-dashboard.html'];
    var page = window.location.pathname.split('/').pop() || 'index.html';
    if (skip.indexOf(page) >= 0) return;
    // Check if already loaded
    if (document.querySelector('script[src="quote-modal.js"]')) return;
    if (typeof openQuoteModal !== 'undefined') return;
    var s = document.createElement('script');
    s.src = 'quote-modal.js';
    document.body.appendChild(s);
  }

  // ── Initialize Everything ──
  function init() {
    initDarkMode();
    injectMobileMenu();
    buildLangDropdown();
    highlightActiveNav();
    autoLoadQuoteModal();
    
    // Apply saved language
    var lang = getCurrentLang();
    document.documentElement.lang = lang;
    if (lang === 'ar') document.documentElement.dir = 'rtl';
    applyTranslations(lang);
    updateHreflangTags(lang);
    if (typeof window.onLanguageChanged === "function") window.onLanguageChanged(lang);

    // Session awareness AFTER i18n (so translations don't overwrite avatar)
    updateNavbarSession();

    // Init scroll animations after a brief delay to let DOM settle
    requestAnimationFrame(function() {
      initScrollAnimations();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
