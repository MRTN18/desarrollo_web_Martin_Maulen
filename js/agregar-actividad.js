const horaInicio = document.getElementById("inicio");
const horaTermino = document.getElementById("termino");

const now = new Date();
const year = now.getFullYear();
const month = String(now.getMonth() + 1).padStart(2, "0");
const day = String(now.getDate()).padStart(2, "0");
const hours = String(now.getHours()).padStart(2, "0");
const minutes = String(now.getMinutes()).padStart(2, "0");
const formattedDate = `${year}-${month}-${day}T${hours}:${minutes}`;

horaInicio.value = formattedDate;
horaTermino.value = formattedDate;

const region = document.getElementById("region");
const comuna = document.getElementById("comuna");
const sector = document.getElementById("sector");
const nombre = document.getElementById("nombre");
const email = document.getElementById("email");
const celular = document.getElementById("celular");
const contactarPor = document.getElementById("contactarPor");
const errorNombre = document.getElementById("errorNombre");
const errorEmail = document.getElementById("errorEmail");
const errorCelular = document.getElementById("errorCelular");
const errorTema = document.getElementById("errorTema");
const errorRegion = document.getElementById("errorRegion");
const errorComuna = document.getElementById("errorComuna");
const errorOtro = document.getElementById("errorOtro");
const errorFoto = document.getElementById("errorFoto");
const errorFecha = document.getElementById("errorFecha");
const errorSector = document.getElementById("errorSector");
const errorRedSocial = document.getElementById("errorRedSocial");
const tema = document.getElementById("tema");
const otroTema = document.getElementById("otroTema");
const inputOtroTema = document.getElementById("inputOtroTema");
const fotos = document.getElementById("fotos");
const botonAgregarFoto = document.getElementById("otraFoto");
const modal = document.getElementById("modalConfirmacion");
const botonAgregarActividad = document.querySelector(
  ".agregarActividad button"
);
const botonConfirmar = document.getElementById("confirmarActividad");
const botonCancelar = document.getElementById("cancelarActividad");
const botonVolver = document.getElementById("btnVolver");
let inputFotos = document.querySelectorAll('input[type="file"]');

// Cerrar el modal al presionar "No"
botonCancelar.addEventListener("click", () => {
  modal.style.display = "none";
});

// Confirmar la acción al presionar "Sí"
botonConfirmar.addEventListener("click", () => {
  modal.style.display = "none";
  window.location.href = "/html/confirmacion-agregar-tarea.html";
});

botonVolver.addEventListener("click", () => {
  window.location.href = "/html/index.html";
});

// Cargar regiones y comunas desde el archivo JSON
fetch("/region_comuna.json")
  .then((response) => response.json())
  .then((data) => {
    const regiones = data.regiones;

    regiones.forEach((regionData) => {
      const option = document.createElement("option");
      option.value = regionData.id;
      option.textContent = regionData.nombre;
      region.appendChild(option);
    });

    region.addEventListener("change", () => {
      const regionSeleccionada = region.value;
      comuna.innerHTML = '<option value="--">--</option>';

      if (regionSeleccionada !== "--") {
        const regionEncontrada = regiones.find(
          (r) => r.id == regionSeleccionada
        );
        if (regionEncontrada) {
          regionEncontrada.comunas.forEach((comunaData) => {
            const option = document.createElement("option");
            option.value = comunaData.id;
            option.textContent = comunaData.nombre;
            comuna.appendChild(option);
          });
        }
        comuna.disabled = false;
      } else {
        comuna.disabled = true;
      }
    });
  })
  .catch((error) =>
    console.error("Error al cargar regiones y comunas:", error)
  );

botonAgregarFoto.addEventListener("click", () => {
  const nuevoInput = document.createElement("input");
  nuevoInput.type = "file";
  nuevoInput.name = "foto" + fotos.childElementCount;
  nuevoInput.onchange = validarFoto;
  fotos.appendChild(nuevoInput);
  inputFotos = document.querySelectorAll('input[type="file"]');
  if (inputFotos.length === 5) {
    botonAgregarFoto.disabled = true;
  }
});

const validarRegion = () => {
  if (region.value === "--") {
    region.style.borderColor = "red";
    region.style.borderRadius = "2px";
    errorRegion.style.display = "block";
    errorRegion.innerText = "¡Debes ingresar una Región!";
    errorRegion.style.color = "red";
    return false;
  } else {
    region.style.borderColor = "";
    region.style.borderRadius = "";
    errorRegion.style.display = "none";
    errorRegion.innerHTML = "";
    return true;
  }
};

const validarComuna = () => {
  if (comuna.value === "--") {
    comuna.style.borderColor = "red";
    comuna.style.borderRadius = "2px";
    errorComuna.style.display = "block";
    errorComuna.innerText = "¡Debes ingresar una Comuna!";
    errorComuna.style.color = "red";
    return false;
  } else {
    comuna.style.borderColor = "";
    comuna.style.borderRadius = "";
    errorComuna.style.display = "none";
    errorComuna.innerHTML = "";
    return true;
  }
};

const validarSector = () => {
  if (sector.value != "" && sector.value.length > 100) {
    sector.style.borderColor = "red";
    sector.style.borderRadius = "2px";
    errorSector.style.display = "block";
    errorSector.innerText = "¡El sector debe tener como máximo 100 caracteres!";
    errorSector.style.color = "red";
    return false;
  } else {
    sector.style.borderColor = "";
    sector.style.borderRadius = "";
    errorSector.style.display = "none";
    errorSector.innerHTML = "";
    return true;
  }
};

const validarNombre = () => {
  if (nombre.value == "") {
    nombre.style.borderColor = "red";
    nombre.style.borderRadius = "2px";
    errorNombre.style.display = "block";
    errorNombre.innerText = "¡Debes ingresar un Nombre!";
    errorNombre.style.color = "red";
    return false;
  } else if (nombre.value.length > 200) {
    nombre.style.borderColor = "red";
    nombre.style.borderRadius = "2px";
    errorNombre.style.display = "block";
    errorNombre.innerText = "¡El nombre debe tener como máximo 200 caracteres!";
    errorNombre.style.color = "red";
    return false;
  } else {
    nombre.style.borderColor = "";
    nombre.style.borderRadius = "";
    errorNombre.style.display = "none";
    errorNombre.innerHTML = "";
    return true;
  }
};

const validarEmail = () => {
  if (email.value == "") {
    email.style.borderColor = "red";
    email.style.borderRadius = "2px";
    errorEmail.style.display = "block";
    errorEmail.innerText = "¡Debes ingresar un Email!";
    errorEmail.style.color = "red";
    return false;
  }
  if (email.value != "") {
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email.value)) {
      email.style.borderColor = "red";
      email.style.borderRadius = "2px";
      errorEmail.style.display = "block";
      errorEmail.innerText = "¡Debes ingresar un email válido!";
      errorEmail.style.color = "red";
      return false;
    } else {
      if (nombre.value.length > 100) {
        nombre.style.borderColor = "red";
        nombre.style.borderRadius = "2px";
        errorNombre.style.display = "block";
        errorNombre.innerText =
          "¡El email debe tener como máximo 100 caracteres!";
        errorNombre.style.color = "red";
        return false;
      } else {
        email.style.borderColor = "";
        email.style.borderRadius = "";
        errorEmail.style.display = "none";
        errorEmail.innerHTML = "";
        return true;
      }
    }
  }
};

const formatearNumero = (numero) => {
  let nuevoNumero = "";
  for (i = 0; i < numero.length; i++) {
    nuevoNumero += numero[i];
    if (i == 3) {
      nuevoNumero += ".";
    }
  }
  return nuevoNumero;
};

const validarTelefono = () => {
  const telefonoRegex = /^\+\d{3}\.\d{8}$/;
  const nuevoNumero = formatearNumero(celular.value);
  if (!telefonoRegex.test(nuevoNumero)) {
    celular.style.borderColor = "red";
    celular.style.borderRadius = "2px";
    errorCelular.style.display = "block";
    errorCelular.innerText = "¡El número de teléfono no es válido!";
    errorCelular.style.color = "red";
    return false;
  } else {
    celular.style.borderColor = "";
    celular.style.borderRadius = "";
    errorCelular.style.display = "none";
    errorCelular.innerHTML = "";
    return true;
  }
};

const validarFechas = () => {
  if (horaInicio.value > horaTermino.value) {
    horaInicio.style.borderColor = "red";
    horaInicio.style.borderRadius = "2px";
    errorFecha.style.display = "block";
    errorFecha.innerText =
      "¡La fecha de inicio no concuerda con la fecha de termino!";
    errorFecha.style.color = "red";
    return false;
  } else {
    horaInicio.style.borderColor = "";
    horaInicio.style.borderRadius = "";
    errorFecha.style.display = "none";
    errorFecha.innerHTML = "";
    return true;
  }
};

const validarRedSocial = () => {
  if (
    contactarPor.value != "" &&
    (contactarPor.value.length < 4 || contactarPor.value.length > 50)
  ) {
    errorRedSocial.style.display = "block";
    errorRedSocial.innerText =
      "¡El ID o URL debe tener como mínimo 4 caracteres y como máximo 50!";
    errorRedSocial.style.color = "red";
    return false;
  } else {
    errorRedSocial.style.display = "none";
    errorRedSocial.innerHTML = "";
    return true;
  }
};

const otroTemaDisplay = () => {
  if (tema.value == "otro") {
    otroTema.style.display = "flex";
  } else {
    otroTema.style.display = "none";
  }
};

tema.addEventListener("change", () => {
  otroTemaDisplay();
});

const validarTema = () => {
  if (tema.value == "--") {
    tema.style.borderColor = "red";
    tema.style.borderRadius = "2px";
    errorTema.style.display = "block";
    errorTema.innerText = "¡Debes ingresar un Tema!";
    errorTema.style.color = "red";
    return false;
  } else {
    tema.style.borderColor = "";
    tema.style.borderRadius = "";
    errorTema.style.display = "none";
    errorTema.innerHTML = "";
    return true;
  }
};

const validarOtroTema = () => {
  if (inputOtroTema.value == "" && tema.value == "otro") {
    inputOtroTema.style.borderColor = "red";
    inputOtroTema.style.borderRadius = "2px";
    errorOtro.style.display = "block";
    errorOtro.innerText = "¡Debes ingresar un Tema!";
    errorOtro.style.color = "red";
    return false;
  } else if (
    (inputOtroTema.value.length < 3 || inputOtroTema.value.length > 15) &&
    tema.value == "otro"
  ) {
    inputOtroTema.style.borderColor = "red";
    inputOtroTema.style.borderRadius = "2px";
    errorOtro.style.display = "block";
    errorOtro.innerText =
      "¡El tema debe tener como mínimo 3 caracteres y como máximo 15!";
    errorOtro.style.color = "red";
    return false;
  } else {
    inputOtroTema.style.borderColor = "";
    inputOtroTema.style.borderRadius = "";
    errorOtro.style.display = "none";
    errorOtro.innerHTML = "";
    return true;
  }
};

const inputsFotosVacios = () => {
  let cantidad = 0;
  inputFotos.forEach((input) => {
    if (input.value === "") cantidad += 1;
  });
  if (cantidad === inputFotos.length) return true;
  else return false;
};

const validarFoto = () => {
  if (inputsFotosVacios()) {
    errorFoto.style.display = "block";
    errorFoto.innerText = "¡Debes ingresar una Foto!";
    errorFoto.style.color = "red";
    return false;
  } else {
    errorFoto.style.display = "none";
    errorFoto.innerHTML = "";
    return true;
  }
};

const validate = () => {
  const email = validarEmail();
  const nombre = validarNombre();
  const region = validarRegion();
  const comuna = validarComuna();
  const telefono = validarTelefono();
  const tema = validarTema();
  const otroTema = validarOtroTema();
  const fotos = validarFoto();
  const fechas = validarFechas();
  const redSocial = validarRedSocial();
  const sector = validarSector();
  if (
    email &&
    nombre &&
    tema &&
    region &&
    comuna &&
    telefono &&
    fotos &&
    otroTema &&
    fechas &&
    redSocial &&
    sector
  ) {
    modal.style.display = "block";
  }
};
