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

  // お問い合わせフォーム：送信先が決まるまではプレビュー表示のみ
  var form = document.querySelector('form[data-preview]');
  if (form) {
    var t = (location.hash || '').replace('#', '');
    if (t) { var r = form.querySelector('input[name="type"][value="' + t + '"]'); if (r) r.checked = true; }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = document.querySelector('.form-msg');
      if (!form.checkValidity()) { form.reportValidity(); return; }
      msg.textContent = '確認用ページのため、まだ送信はされません。公開時に送信先（メール）を設定します。';
      msg.classList.add('show');
      msg.scrollIntoView({ block: 'center' });
    });
  }
})();
