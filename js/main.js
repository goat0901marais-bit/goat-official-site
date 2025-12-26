// =======================
// Swiper（メインビジュアル）
// =======================
const swiper = new Swiper('.swiper', {
  loop: true,
  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },
  effect: 'fade',
  speed: 1000,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});


// =======================
// スクロールアニメーション
// =======================
document.addEventListener("DOMContentLoaded", () => {
  const targets = document.querySelectorAll(".popup");

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    threshold: 0.4,
    rootMargin: "0px"
  });

  targets.forEach(target => observer.observe(target));
});
