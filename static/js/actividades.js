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
