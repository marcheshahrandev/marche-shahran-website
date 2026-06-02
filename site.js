/* Marché Shahran — shared site behaviour */
(function () {
  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  var backdrop = document.getElementById('backdrop');
  function close() {
    if (!nav) return;
    nav.classList.remove('open');
    if (backdrop) backdrop.classList.remove('open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      if (backdrop) backdrop.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', String(open));
    });
  }
  if (backdrop) backdrop.addEventListener('click', close);
  if (nav) nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', close); });

  // Scroll reveal (scroll-based for reliability across preview/embed contexts)
  var els = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  function check() {
    var h = window.innerHeight || document.documentElement.clientHeight;
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.classList.contains('in')) continue;
      var r = el.getBoundingClientRect();
      if (r.top < h * 0.92 && r.bottom > 0) el.classList.add('in');
    }
  }
  check();
  window.addEventListener('scroll', check, { passive: true });
  window.addEventListener('resize', check);
  window.addEventListener('load', function () { setTimeout(check, 60); });
  // absolute safety net — never leave content hidden
  setTimeout(function () { els.forEach(function (el) { el.classList.add('in'); }); }, 1400);
})();
