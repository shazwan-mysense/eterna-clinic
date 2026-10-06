/* ÉTERNA CLINIC — shared behaviours.
   Each block notes its Elementor Pro equivalent for the rebuild. */

(function () {
  'use strict';

  /* Sticky header shadow + shrink (Elementor: sticky header + scroll class) */
  const header = document.querySelector('.header');
  const onScroll = () => {
    if (!header) return;
    header.classList.toggle('is-stuck', window.scrollY > 10);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Mobile nav */
  const burger = document.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', () => document.body.classList.toggle('nav-open'));
    document.querySelectorAll('.nav a').forEach(a =>
      a.addEventListener('click', () => document.body.classList.remove('nav-open'))
    );
  }

  /* Reveal on scroll (Elementor: entrance animations fadeInUp / zoomIn) */
  const revealables = document.querySelectorAll('.reveal, .reveal-zoom');
  if ('IntersectionObserver' in window && revealables.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in-view');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealables.forEach(el => io.observe(el));
  } else {
    revealables.forEach(el => el.classList.add('in-view'));
  }

  /* Carousels (Elementor: loop carousel / testimonial carousel) */
  document.querySelectorAll('[data-carousel]').forEach(root => {
    const track = root.querySelector('.carousel__track');
    const prev = root.querySelector('[data-prev]');
    const next = root.querySelector('[data-next]');
    if (!track) return;
    const stepSize = () => {
      const card = track.children[0];
      if (!card) return 0;
      const gap = parseFloat(getComputedStyle(track).columnGap || 32);
      return card.getBoundingClientRect().width + gap;
    };
    const update = () => {
      if (prev) prev.disabled = track.scrollLeft <= 4;
      if (next) next.disabled = track.scrollLeft >= track.scrollWidth - track.clientWidth - 4;
    };
    prev && prev.addEventListener('click', () => track.scrollBy({ left: -stepSize(), behavior: 'smooth' }));
    next && next.addEventListener('click', () => track.scrollBy({ left: stepSize(), behavior: 'smooth' }));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  /* Accordions (Elementor: accordion widget) */
  document.querySelectorAll('.accordion').forEach(acc => {
    acc.querySelectorAll('.acc-item').forEach(item => {
      const head = item.querySelector('.acc-item__head');
      const body = item.querySelector('.acc-item__body');
      if (!head || !body) return;
      head.addEventListener('click', () => {
        const isOpen = item.classList.contains('is-open');
        acc.querySelectorAll('.acc-item.is-open').forEach(o => {
          o.classList.remove('is-open');
          o.querySelector('.acc-item__body').style.maxHeight = null;
        });
        if (!isOpen) {
          item.classList.add('is-open');
          body.style.maxHeight = body.scrollHeight + 'px';
        }
      });
    });
    /* open the first item by default */
    const first = acc.querySelector('.acc-item');
    if (first) {
      first.classList.add('is-open');
      const b = first.querySelector('.acc-item__body');
      if (b) b.style.maxHeight = b.scrollHeight + 'px';
    }
  });

  /* Count-up stats (Elementor: counter widget) */
  const counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window && counters.length) {
    const cio = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = parseInt(el.dataset.count, 10);
        const suffix = el.dataset.suffix || '';
        const dur = 1600;
        const t0 = performance.now();
        const tick = (t) => {
          const p = Math.min((t - t0) / dur, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased).toLocaleString() + suffix;
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        /* guarantee the final value even if rAF is throttled */
        setTimeout(() => { el.textContent = target.toLocaleString() + suffix; }, dur + 150);
        cio.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(el => cio.observe(el));
  }

  /* Custom cursor dot (theme feature in Pure Skin; HTML-widget snippet in WP) */
  const dot = document.createElement('div');
  const ring = document.createElement('div');
  dot.className = 'cursor-dot';
  ring.className = 'cursor-ring';
  document.body.append(dot, ring);
  let mx = -100, my = -100, rx = -100, ry = -100;
  window.addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; }, { passive: true });
  (function loop() {
    rx += (mx - rx) * 0.16;
    ry += (my - ry) * 0.16;
    dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%,-50%)`;
    ring.style.transform = `translate(${rx}px, ${ry}px) translate(-50%,-50%)`;
    requestAnimationFrame(loop);
  })();
  document.querySelectorAll('a, button, .svc-card, .person').forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
  });

  /* Demo form handler — no backend in this mockup */
  document.querySelectorAll('form[data-demo]').forEach(f => {
    f.addEventListener('submit', (e) => {
      e.preventDefault();
      const note = f.querySelector('.form-note');
      if (note) note.textContent = 'Thank you — this is a design mockup, so no booking was sent. The live site will connect this form to the clinic.';
    });
  });
})();
