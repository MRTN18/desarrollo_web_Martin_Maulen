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