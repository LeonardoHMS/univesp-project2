// Slideshow automático
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
  setTimeout(showSlides, 5000); // Muda a cada 5 segundos
}

function currentSlide(n) {
  slideIndex = n;
  showSlides();
}

// Navegação suave
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
anchor.addEventListener('click', function(e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute('href'));
    target.scrollIntoView({
    behavior: 'smooth'
    });
});
});

// Botão de voltar ao topo
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