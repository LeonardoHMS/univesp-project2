let slideIndex = 0;
showSlides();

function showSlides() {
  let slides = document.getElementsByClassName("slide");
  let dots = document.getElementsByClassName("dot");
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) { slideIndex = 1 }    
  for (let i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 5000);
}

function currentSlide(n) {
  slideIndex = n;
  showSlides();
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
anchor.addEventListener('click', function(e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute('href'));
    target.scrollIntoView({
    behavior: 'smooth'
    });
});
});

const backToTopButton = document.getElementById('back-to-top');

window.onscroll = function() {
if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    backToTopButton.style.display = 'block';
} else {
    backToTopButton.style.display = 'none';
}
};

backToTopButton.addEventListener('click', function() {
window.scrollTo({
    top: 0,
    behavior: 'smooth'
});
});

let gallerySlideIndex = 1;
showGallerySlides(gallerySlideIndex);

function currentGallerySlide(n) {
  showGallerySlides(gallerySlideIndex = n);
}

function showGallerySlides(n) {
  let i;
  let slides = document.getElementsByClassName("gallery-slide");
  let dots = document.getElementsByClassName("gallery-dot");

  if (n > slides.length) { gallerySlideIndex = 1 }
  if (n < 1) { gallerySlideIndex = slides.length }

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" gallery-active", "");
  }

  slides[gallerySlideIndex - 1].style.display = "block";
  dots[gallerySlideIndex - 1].className += " gallery-active";
}

document.addEventListener('DOMContentLoaded', function() {
  var swiper = new Swiper(".mySwiper", {
      slidesPerView: 1,
      spaceBetween: 30,
      loop: true,
      pagination: {
          el: ".swiper-pagination",
          clickable: true,
      },
      navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
      },
      autoplay: {
          delay: 4000,
          disableOnInteraction: false,
      },
      effect: 'slide',
      speed: 1000,
  });
});