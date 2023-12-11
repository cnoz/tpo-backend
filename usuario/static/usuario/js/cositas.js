/* CARRUSEL */
const slides = document.querySelectorAll('.carruseles');
let slideActual = 0;

function carrusel() {
  slides.forEach((slide, i) => {
    if (i === slideActual) {
      slide.classList.remove('izquierda', 'derecha');
      slide.classList.add('centro');
    } else if (i < slideActual) {
        slide.classList.remove('centro', 'derecha');
        slide.classList.add('izquierda');
    } else {
        slide.classList.remove('centro', 'izquierda');
        slide.classList.add('derecha');
    }
  });
}

function siguiente() {
  slideActual = (slideActual + 1) % slides.length;
  carrusel();
}
function anterior() {
  slideActual = (slideActual - 1 + slides.length) % slides.length;
  carrusel();
}
document.getElementById('botonSiguiente').addEventListener('click', siguiente);
document.getElementById('botonAnterior').addEventListener('click', anterior);

carrusel();


/* VALIDACIÓN FORMULARIO */
var nombre  = document.getElementById("nombre");
var email  = document.getElementById("email");
var mensaje  = document.getElementById("mensaje");
var form = document.getElementById("formulario");

form.addEventListener("submit", function(event){
  console.log("formulario funcionando");
  event.preventDefault();
  var mensajeError = [];
  
  if ( nombre.value === null || nombre.value === ""){
    mensajeError.push("el campo nombre está vacio");
  }
  if (email.value === null || email.value == ""){
    mensajeError.push("el campo email está vacio");
  }
  error.innerHTML = mensajeError.join(', ');
  return false;
});



