(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.gnav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  // お問い合わせフォーム：本番ドメイン以外（確認用ページ）では送信しない
  var form = document.querySelector('.form');
  if (form) {
    var t = (location.hash || '').replace('#', '');
    if (t) { var r = form.querySelector('input[data-key="' + t + '"]'); if (r) r.checked = true; }
    var live = /(^|\.)marais\.co\.jp$|github\.io$/.test(location.hostname);
    if (!live) form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = document.querySelector('.form-msg');
      if (!form.checkValidity()) { form.reportValidity(); return; }
      msg.textContent = '確認用ページのため送信されません。公開後のサイトでは r.nagai@marais.co.jp に届きます。';
      msg.classList.add('show');
      msg.scrollIntoView({ block: 'center' });
    });
  }
})();
