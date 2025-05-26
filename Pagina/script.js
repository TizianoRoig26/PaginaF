document.addEventListener("DOMContentLoaded", function() {
    const botonReservar = document.querySelector(".reservar-btn");
    
    botonReservar.addEventListener("click", function(event) {
        event.preventDefault();
        
        const confirmacion = confirm("¿Quieres confirmar tu reserva?");
        if (confirmacion) {
            alert("¡Reserva realizada con éxito! Nos pondremos en contacto contigo.");
            window.location.href = "formulario.html";
        } else {
            alert("Reserva cancelada.");
        }
    });
});