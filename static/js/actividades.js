const form = document.getElementById("formulario");
const nombre = document.getElementById("nombre");
const comentario = document.getElementById("comentario");
const formulario_comentario = document.getElementById("formulario-comentario");
const agregar_comentario = document.getElementById("agregar-comentario");

function validarFormulario() {
  if (nombre.value.trim() === "") {
    alert("Por favor, ingresa tu nombre.");
    return false;
  }
  if (comentario.value.trim() === "") {
    alert("Por favor, escribe un comentario.");
    return false;
  }
  if (nombre.value.length > 80 || nombre.value.length < 3) {
    alert("El nombre debe tener entre 3 y 80 caracteres.");
    return false;
  }
  if (comentario.value.length < 5) {
    alert("El comentario debe tener al menos 5 caracteres.");
    return false;
  }
  return true;
}

agregar_comentario.addEventListener("click", () => {
  formulario_comentario.style.display = "flex";
  agregar_comentario.style.display = "none";
});

document.getElementById("crear-comentario").addEventListener("click", () => {
  if (validarFormulario()) {
    form.submit();
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const images = document.querySelectorAll(".fotos-actividad img");
  const modal = document.createElement("div");
  const modalImg = document.createElement("img");
  const closeButton = document.createElement("button");

  modal.style.position = "fixed";
  modal.style.top = "0";
  modal.style.left = "0";
  modal.style.width = "100%";
  modal.style.height = "100%";
  modal.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
  modal.style.display = "none";
  modal.style.justifyContent = "center";
  modal.style.alignItems = "center";
  modal.style.zIndex = "1000";

  modalImg.style.width = "800px";
  modalImg.style.height = "600px";
  modalImg.src = "init";
  modalImg.alt = "Imagen de la actividad";

  closeButton.textContent = "X";
  closeButton.style.position = "absolute";
  closeButton.style.top = "20px";
  closeButton.style.right = "20px";
  closeButton.style.padding = "10px 20px";
  closeButton.style.backgroundColor = "#fff";
  closeButton.style.border = "none";
  closeButton.style.cursor = "pointer";

  modal.appendChild(modalImg);
  modal.appendChild(closeButton);
  document.body.appendChild(modal);

  // Evento para mostrar el modal
  images.forEach((img) => {
    img.addEventListener("click", () => {
      modalImg.src = img.src;
      modal.style.display = "flex";
    });
  });

  // Evento para cerrar el modal
  closeButton.addEventListener("click", () => {
    modal.style.display = "none";
  });
});

fetch("http://127.0.0.1:5000/get-coments")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Error en la respuesta del servidor");
    }
    return response.json();
  })
  .then((data) => {
    const url = window.location.href;
    const actividadId = url.split("/").pop();
    console.log(data);

    const comentariosContainer = document.getElementById("comentarios");
    data.forEach((comentario) => {
      if (comentario.actividad_id === Number(actividadId)) {
        const nuevo_comentario = document.createElement("div");
        nuevo_comentario.className = "comentario";
        const nombre = document.createElement("h3");
        const comentarioTexto = document.createElement("p");
        const fecha = document.createElement("div");

        nombre.textContent = comentario.nombre;
        comentarioTexto.textContent = comentario.texto;
        fecha.textContent = new Date(comentario.fecha).toLocaleString();

        nuevo_comentario.appendChild(nombre);
        nuevo_comentario.appendChild(comentarioTexto);
        nuevo_comentario.appendChild(fecha);
        comentariosContainer.prepend(nuevo_comentario);
      }
    });
  })
  .catch((error) => {
    console.error("Error al cargar los comentarios:", error);
    const comentariosContainer = document.getElementById("comentarios");
    const errorDiv = document.createElement("div");
    errorDiv.textContent = "No se pudieron cargar los comentarios.";
    comentariosContainer.appendChild(errorDiv);
  });
