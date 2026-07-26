(function () {
  // ---- copy buttons on code blocks ----
  document.querySelectorAll('.copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var code = btn.parentElement.querySelector('code');
      if (!code) return;
      navigator.clipboard.writeText(code.innerText).then(function () {
        btn.textContent = 'Copied';
        btn.classList.add('done');
        setTimeout(function () {
          btn.textContent = 'Copy';
          btn.classList.remove('done');
        }, 1600);
      }).catch(function () {
        btn.textContent = 'Press \u2318C';
        setTimeout(function () { btn.textContent = 'Copy'; }, 1600);
      });
    });
  });

  // ---- highlight the section you're reading (index page only) ----
  var links = Array.prototype.slice.call(document.querySelectorAll('#nav a'));
  var map = {};
  links.forEach(function (a) {
    var href = a.getAttribute('href') || '';
    var hash = href.indexOf('#');
    if (hash === -1) return;
    var id = href.slice(hash + 1);
    var el = document.getElementById(id);
    if (el) map[id] = a;
  });

  if (Object.keys(map).length) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.classList.remove('on'); });
          if (map[e.target.id]) map[e.target.id].classList.add('on');
        }
      });
    }, { rootMargin: '-10% 0px -80% 0px', threshold: 0 });
    Object.keys(map).forEach(function (id) { obs.observe(document.getElementById(id)); });
  }

  // ---- mobile drawer ----
  var sb = document.getElementById('sidebar');
  var veil = document.getElementById('veil');
  var menu = document.getElementById('menu');
  function close() { sb.classList.remove('open'); veil.classList.remove('show'); }
  if (menu) {
    menu.addEventListener('click', function () {
      sb.classList.toggle('open');
      veil.classList.toggle('show');
    });
  }
  if (veil) veil.addEventListener('click', close);
  links.forEach(function (a) {
    a.addEventListener('click', function () { if (window.innerWidth <= 920) close(); });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
})();
