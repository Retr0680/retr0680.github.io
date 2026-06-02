// Retr0's Library — theme JS
(function () {
  'use strict';

  // Mobile nav toggle
  var toggle = document.getElementById('nav-toggle');
  var links  = document.getElementById('nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
  }

  // "/" key focuses search bar
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {
      e.preventDefault();
      var bar = document.querySelector('.r-search-bar');
      if (bar) bar.focus();
    }
  });

  // Live post filtering via search bar
  var bar = document.querySelector('.r-search-bar');
  if (bar) {
    bar.addEventListener('input', function () {
      var q = bar.value.toLowerCase().trim();
      var cards = document.querySelectorAll('.post-card');
      cards.forEach(function (card) {
        var text = card.textContent.toLowerCase();
        card.style.display = (!q || text.includes(q)) ? '' : 'none';
      });
    });
  }
})();
