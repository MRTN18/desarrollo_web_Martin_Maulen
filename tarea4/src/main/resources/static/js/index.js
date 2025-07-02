function evaluar(index) {
    const evaluarButton = document.getElementById(`evaluar${index}`);
    const notaInput = document.getElementById(`nota${index}`);
    const enviarButton = document.getElementById(`enviar${index}`);
    evaluarButton.style.display = 'none';
    notaInput.style.display = 'inline-block';
    enviarButton.style.display = 'inline-block';
}

function cambiarNota (index) {
    if (Number(document.getElementById(`nota${index}`).value) < 1) {
        document.getElementById(`nota${index}`).value = 1;
        return;
    } else if (Number(document.getElementById(`nota${index}`).value) > 7) {
        document.getElementById(`nota${index}`).value = 7;
        return;
    }
}

function enviar(index) {
    const form = document.getElementById(`form${index}`);
    form.submit();
}

async function calcularPromedioNotas(actividadId, index) {
    try {
        // Hacer fetch a la API para obtener las notas de la actividad
        const response = await fetch(`/get-notas/${actividadId}`);
        if (!response.ok) {
            throw new Error("Error al obtener las notas");
        }

        const notasResponse = await response.json(); // Convertir la respuesta a JSON
        const notas = notasResponse.data;

        console.log(notas);

        // Calcular el promedio
        const sumaNotas = notas.reduce((acc, nota) => acc + nota.nota, 0);
        let promedio = Math.round(sumaNotas / notas.length); // Redondear a número entero

        // Si el promedio es NaN (por ejemplo, no hay notas), mostrar "--"
        if (isNaN(promedio)) {
            promedio = "--";
        }

        // Mostrar el promedio en la columna correspondiente
        const promedioElement = document.getElementById(`nota-promedio-${index}`);
        if (promedioElement) {
            promedioElement.textContent = promedio;
        } else {
            console.error(`Elemento con id nota-promedio-${index} no encontrado`);
        }
    } catch (error) {
        console.error("Error al calcular el promedio de notas:", error);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const actividades = document.querySelectorAll(".actividad-row"); // Usar la clase como selector
    actividades.forEach((actividad, index) => {
        const actividadId = actividad.querySelector("td:first-child").textContent; // Obtener el ID de la actividad
        calcularPromedioNotas(actividadId, index);
    });
});