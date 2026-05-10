/* ═══════════════════════════════════════════════════════════════
   MediRoute Performance Module
   - Intersection Observer for fade-in animations
   - Debounced scroll/resize handlers
   - Resource loading optimization
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ── 1. Intersection Observer for scroll-reveal animations ── */
  function initFadeObserver() {
    // Only target elements that explicitly opt in with data-animate
    const els = document.querySelectorAll('[data-animate]');
    if (!els.length) return;

    if ('IntersectionObserver' in window) {
      const obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

      els.forEach(function (el) {
        // Elements already in viewport get shown immediately
        var rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
          el.classList.add('fade-observed', 'is-visible');
        } else {
          el.classList.add('fade-observed');
          obs.observe(el);
        }
      });
    } else {
      // Fallback: just show everything
      els.forEach(function (el) { el.classList.add('is-visible'); });
    }
  }

  /* ── 2. Debounce utility ── */
  function debounce(fn, ms) {
    var timer;
    return function () {
      var ctx = this, args = arguments;
      clearTimeout(timer);
      timer = setTimeout(function () { fn.apply(ctx, args); }, ms);
    };
  }

  /* ── 3. Optimized scroll handler ── */
  function initScrollOptimization() {
    // Use passive listeners for scroll performance
    var scrollHandlers = [];
    window.__MR_onScroll = function (fn) { scrollHandlers.push(fn); };

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          scrollHandlers.forEach(function (fn) { fn(); });
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });

    // Touch listeners as passive
    document.addEventListener('touchstart', function () {}, { passive: true });
    document.addEventListener('touchmove', function () {}, { passive: true });
  }

  /* ── 4. Prefetch visible links on hover ── */
  function initLinkPrefetch() {
    if (!('IntersectionObserver' in window)) return;

    var prefetched = {};
    document.addEventListener('mouseover', function (e) {
      var link = e.target.closest('a[href]');
      if (!link) return;
      var href = link.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('javascript') ||
          href.startsWith('http') || prefetched[href]) return;

      // Only prefetch local .html files
      if (href.endsWith('.html')) {
        prefetched[href] = true;
        var el = document.createElement('link');
        el.rel = 'prefetch';
        el.href = href;
        document.head.appendChild(el);
      }
    });
  }

  /* ── 5. Reduce motion for users who prefer it ── */
  function initReducedMotion() {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.documentElement.classList.add('reduce-motion');
    }
  }

  /* ── 6. Font loading optimization ── */
  function initFontOptimization() {
    if ('fonts' in document) {
      document.fonts.ready.then(function () {
        document.documentElement.classList.add('fonts-loaded');
      });
    } else {
      // Fallback
      setTimeout(function () {
        document.documentElement.classList.add('fonts-loaded');
      }, 1000);
    }
  }

  /* ── 7. Back/forward cache optimization ── */
  function initBFCache() {
    window.addEventListener('pageshow', function (e) {
      if (e.persisted) {
        // Page was restored from BF cache — re-run i18n if needed
        if (typeof window.applyLanguage === 'function') {
          window.applyLanguage(localStorage.getItem('mediroute-lang') || 'en');
        }
      }
    });
  }

  /* ── Init on DOMContentLoaded ── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    initFadeObserver();
    initScrollOptimization();
    initLinkPrefetch();
    initReducedMotion();
    initFontOptimization();
    initBFCache();
  }

  // Expose debounce utility globally
  window.__MR_debounce = debounce;

})();
