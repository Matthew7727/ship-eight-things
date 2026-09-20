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
        btn.textContent = 'Copy manually';
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
          // ---- save progress ----
          saveProgress(e.target.id);
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

  // ---- progress tracking (pick up where you left off) ----
  var STORAGE_KEY = 'shipEightGuideProgress';

  function pageTitle() {
    return document.title || '';
  }

  function currentPagePath() {
    // Normalise to a root-relative path so it works regardless of origin
    return window.location.pathname;
  }

  function saveProgress(sectionId) {
    try {
      var sectionEl = document.getElementById(sectionId);
      var heading = sectionEl ? sectionEl.querySelector('h2, h3') : null;
      var sectionTitle = heading ? heading.textContent.trim() : sectionId;
      var data = {
        path: currentPagePath(),
        hash: sectionId ? '#' + sectionId : '',
        pageTitle: pageTitle(),
        sectionTitle: sectionTitle,
        ts: Date.now()
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (e) { /* localStorage may be unavailable */ }
  }

  // Save that we visited this page (without a specific section) on first load
  // so even a quick visit to a page is tracked.
  (function seedPageVisit() {
    try {
      var existing = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
      // Only overwrite if this page is different or there's no record yet
      if (!existing || existing.path !== currentPagePath()) {
        // Don't overwrite if there's a more specific (section-level) save on
        // the same page – that would be a step backwards.
        var data = {
          path: currentPagePath(),
          hash: window.location.hash || '',
          pageTitle: pageTitle(),
          sectionTitle: '',
          ts: Date.now()
        };
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
      }
    } catch (e) { /* ignore */ }
  })();

  // Expose a helper for the welcome page to read progress
  window.ShipEightGuide = {
    getProgress: function () {
      try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null'); }
      catch (e) { return null; }
    },
    clearProgress: function () {
      try { localStorage.removeItem(STORAGE_KEY); } catch (e) { /* ignore */ }
    }
  };
})();
