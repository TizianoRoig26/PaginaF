document.querySelector('form').addEventListener('submit', function(event) {
    // Evitar el envío del formulario hasta validar
    event.preventDefault();
  
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('Apellido').value;
    const email = document.getElementById('email').value;
    const telefono = document.getElementById('telefono').value;
    const actividad = document.getElementById('actividad').value;
    const fecha = document.getElementById('fecha').value;
    const personas = document.getElementById('personas').value;
  
    // Validación simple de los campos
    if (nombre && apellido && email && telefono && actividad && fecha && personas) {
      // Si todos los campos son válidos, enviar el formulario
      alert('¡Reserva realizada con éxito! HOLA MUNDO');
    } else {
      // Si falta algún campo, mostrar mensaje de error
      alert('Por favor, completa todos los campos antes de enviar.');
    }
  });
  