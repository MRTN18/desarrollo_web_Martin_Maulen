const row1 = document.getElementById("row1");
const row2 = document.getElementById("row2");
const row3 = document.getElementById("row3");
const row4 = document.getElementById("row4");
const row5 = document.getElementById("row5");

const redirect = (actividad_id) => {
  window.location.href = `actividades/${actividad_id}`;
};

const mouseEnter = (row) => {
  row.style.cursor = "pointer";
  row.style.background = "rgb(0, 0, 0, 0.2)";
};

const mouseLeave = (row) => {
  row.style.background = "white";
};

document.addEventListener("DOMContentLoaded", function () {
  const rowsPerPage = 5; // Número de filas por página
  const table = document.getElementById("tabla-actividades");
  const rows = Array.from(table.querySelectorAll("tr.dato"));
  const pagination = document.getElementById("pagination");

  function displayPage(page) {
    const start = (page - 1) * rowsPerPage;
    const end = start + rowsPerPage;

    rows.forEach((row, index) => {
      row.style.display = index >= start && index < end ? "" : "none";
    });
  }

  function setupPagination() {
    const pageCount = Math.ceil(rows.length / rowsPerPage);
    pagination.innerHTML = "";

    for (let i = 1; i <= pageCount; i++) {
      const button = document.createElement("button");
      button.textContent = i;
      button.classList.add("page-btn");
      button.addEventListener("click", () => {
        displayPage(i);
        document.querySelectorAll(".page-btn").forEach(btn => btn.classList.remove("active"));
        button.classList.add("active");
      });
      pagination.appendChild(button);
    }

    // Marca el primer botón como activo por defecto
    if (pagination.firstChild) {
      pagination.firstChild.classList.add("active");
    }
  }

  // Inicializa la tabla y la paginación
  displayPage(1);
  setupPagination();
});