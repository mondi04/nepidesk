/**
 * belchenstrasse5.de · main.js
 * - Parallax (Hero)
 * - Scroll Reveal (IntersectionObserver, staggered)
 * - Toast auto-dismiss
 * - Clipboard copy
 */

// ── Parallax ──────────────────────────────────────────────
(function initParallax() {
  const layers = document.querySelectorAll('[data-speed]');
  if (!layers.length) return;

  let ticking = false;

  function applyParallax() {
    const scrollY = window.scrollY;
    layers.forEach(el => {
      const speed = parseFloat(el.dataset.speed) || 0.3;
      el.style.transform = `translateY(${scrollY * speed}px)`;
    });
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(applyParallax);
      ticking = true;
    }
  }, { passive: true });
})();


// ── Scroll Reveal ─────────────────────────────────────────
(function initReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;

      const el = entry.target;
      const delay = parseInt(el.dataset.delay) || 0;

      setTimeout(() => {
        el.classList.add('visible');
      }, delay);

      observer.unobserve(el);
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px',
  });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
})();


// ── Toast auto-dismiss ────────────────────────────────────
document.body.addEventListener('htmx:afterSwap', () => {
  const toast = document.querySelector('#toast-slot .toast[data-duration]');
  if (!toast) return;
  const ms = parseInt(toast.dataset.duration) || 2500;
  setTimeout(() => {
    toast.style.transition = 'opacity .3s';
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 320);
  }, ms);
});


// ── Clipboard copy ────────────────────────────────────────
document.body.addEventListener('click', e => {
  const btn = e.target.closest('.svc-copy');
  if (!btn) return;
  const url = btn.dataset.url;
  if (!url) return;
  navigator.clipboard.writeText(url).catch(() => {});
});


// ── Subtle header shadow on scroll ───────────────────────
(function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (ticking) return;
    requestAnimationFrame(() => {
      if (window.scrollY > 20) {
        header.style.boxShadow = '0 8px 40px rgba(0,0,0,.6)';
      } else {
        header.style.boxShadow = 'none';
      }
      ticking = false;
    });
    ticking = true;
  }, { passive: true });
})();