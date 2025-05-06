from flask import Flask, redirect, render_template, request, url_for
from database import db
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuración de la carpeta de subida
UPLOAD_FOLDER = 'static/image'  # Carpeta donde se guardarán las imágenes
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegúrate de que la carpeta exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/' ,methods=['GET'])
def index():
    if request.method == 'GET':
        actividades = db.get_actividades()[:5]
        data = []
        for actividad in actividades:
            comuna = db.get_comuna_by_id(actividad.comuna_id)
            foto = db.get_foto_by_actividad_id(actividad.id)
            data.append({
                'sector': actividad.sector,
                'dia_hora_inicio': actividad.dia_hora_inicio,
                'dia_hora_termino': actividad.dia_hora_termino,
                'tema': actividad.nombre,
                'comuna': comuna.nombre,
                'foto': foto.ruta_archivo
            })
        return render_template('index.html', data=data)

@app.route('/agregar-actividad', methods=['GET', 'POST'])
def agregar_actividad():
    if request.method == 'POST':
        region = request.form.get('region')
        comuna = request.form.get('comuna')
        sector = request.form.get('sector')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        red_social = request.form.get('contactarPor')
        dia_hora_inicio = request.form.get('inicio')
        dia_hora_termino = request.form.get('termino')
        celular = request.form.get('celular')
        descripcion = request.form.get('descripcion')
        fotos = []
        ruta_fotos = []
        for i in range(0, 5):
            fotos.append(request.files.get('foto' + str(i + 1), ''))
        for foto in fotos:
            if foto and foto.filename != '':
                filename = secure_filename(foto.filename)
                ruta_archivo = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                foto.save(ruta_archivo)
                ruta_relativa = ruta_archivo.replace('static/', '', 1)
                ruta_fotos.append(ruta_relativa)
        tema = request.form.get('tema')
        otroTema = request.form.get('inputOtroTema', '').strip()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('agregar-actividad.html')

@app.route('/actividades')
def actividades():
    return render_template('lista-actividades.html')

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

if __name__ == '__main__':
    app.run(debug=True)