const row1 = document.getElementById("row1");
const row2 = document.getElementById("row2");
const row3 = document.getElementById("row3");
const row4 = document.getElementById("row4");
const row5 = document.getElementById("row5");

const redirect = (actividad) => {
  window.location.href = `/html/actividad${actividad}.html`;
};

const mouseEnter = (row) => {
  row.style.cursor = "pointer";
  row.style.background = "rgb(0, 0, 0, 0.2)";
};

const mouseLeave = (row) => {
  row.style.background = "white";
};
