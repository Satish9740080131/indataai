/* ============================================
   InDataAI Clone — Main JavaScript
   ============================================ */
(function () {
    'use strict';

    /* ── Preloader ── */
    var preloader = document.getElementById('preloader');
    if (preloader) {
        var loaderHidden = false;
        function hideLoader() {
            if (loaderHidden) return;
            loaderHidden = true;
            preloader.classList.add('hide');
            setTimeout(function () { preloader.style.display = 'none'; }, 500);
        }
        // Hide as soon as DOM is ready (don't wait for external CDN resources)
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', hideLoader);
        } else {
            hideLoader();
        }
        // Fallback: force hide after 1.5s no matter what
        setTimeout(hideLoader, 1500);
    }

    document.addEventListener('DOMContentLoaded', function () {

        /* ── Sticky navbar shadow on scroll ── */
        var nav = document.getElementById('mainNav');
        if (nav) {
            window.addEventListener('scroll', function () {
                nav.style.boxShadow = window.scrollY > 50
                    ? '0 4px 24px rgba(0,0,0,0.13)'
                    : '0 2px 15px rgba(0,0,0,0.08)';
            }, { passive: true });
        }

        /* ── Back to top ── */
        var btn = document.getElementById('backToTop');
        if (btn) {
            window.addEventListener('scroll', function () {
                btn.classList.toggle('show', window.scrollY > 300);
            }, { passive: true });
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }

        /* ── Auto-dismiss alerts after 5 s ── */
        document.querySelectorAll('.alert').forEach(function (el) {
            setTimeout(function () {
                el.style.transition = 'opacity .4s';
                el.style.opacity = '0';
                setTimeout(function () { el.remove(); }, 400);
            }, 5000);
        });

        /* ── Close mobile navbar on link click ── */
        var collapse = document.getElementById('navbarNav');
        if (collapse) {
            collapse.querySelectorAll('.nav-link').forEach(function (link) {
                link.addEventListener('click', function () {
                    if (collapse.classList.contains('show')) {
                        var bs = bootstrap.Collapse.getInstance(collapse);
                        if (bs) bs.hide();
                    }
                });
            });
        }

        /* ── Scroll-reveal ── */
        if ('IntersectionObserver' in window) {
            var io = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        io.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

            document.querySelectorAll(
                '.service-card,.testimonial-card,.product-card,.why-card,' +
                '.process-card,.service-page-card,.contact-info-card,' +
                '.portfolio-card,.event-card,.faq-item,.reveal'
            ).forEach(function (el, i) {
                el.classList.add('reveal');
                el.style.transitionDelay = (i % 4) * 0.07 + 's';
                io.observe(el);
            });
        }

        /* ── Counter animation ── */
        var counters = document.querySelectorAll('[data-count]');
        if (counters.length && 'IntersectionObserver' in window) {
            var co = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (!entry.isIntersecting) return;
                    var el = entry.target;
                    var target = parseInt(el.getAttribute('data-count'), 10);
                    var suffix = el.getAttribute('data-suffix') || '';
                    var start = null;
                    function step(ts) {
                        if (!start) start = ts;
                        var p = Math.min((ts - start) / 1400, 1);
                        var ease = 1 - Math.pow(1 - p, 3);
                        el.textContent = Math.floor(ease * target) + suffix;
                        if (p < 1) requestAnimationFrame(step);
                        else el.textContent = target + suffix;
                    }
                    requestAnimationFrame(step);
                    co.unobserve(el);
                });
            }, { threshold: 0.6 });
            counters.forEach(function (el) { co.observe(el); });
        }

        /* ── Newsletter: prevent empty submit ── */
        document.querySelectorAll('.newsletter-form-group, .footer-newsletter-form').forEach(function (form) {
            var parent = form.closest('form') || form;
            parent.addEventListener('submit', function (e) {
                var inp = parent.querySelector('input[type="email"]');
                if (inp && !inp.value.trim()) {
                    e.preventDefault();
                    inp.style.outline = '2px solid #dc3545';
                    inp.focus();
                    setTimeout(function () { inp.style.outline = ''; }, 2000);
                }
            });
        });

        /* ── Contact form: spinner on submit ── */
        var cf = document.querySelector('.contact-form');
        if (cf) {
            cf.addEventListener('submit', function () {
                var sb = cf.querySelector('button[type="submit"]');
                if (sb) {
                    sb.disabled = true;
                    sb.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending…';
                }
            });
        }

        /* ── Quote form: collect checkboxes ── */
        var checkboxes = document.querySelectorAll('input[name="svc"]');
        var hiddenSvc  = document.querySelector('input[name="services"]');
        if (checkboxes.length && hiddenSvc) {
            function syncServices() {
                var vals = [];
                checkboxes.forEach(function (cb) { if (cb.checked) vals.push(cb.value); });
                hiddenSvc.value = vals.join(', ');
            }
            checkboxes.forEach(function (cb) { cb.addEventListener('change', syncServices); });
        }

    });
}());
