import datetime
import hashlib
from flask import Flask, redirect, render_template, request, url_for, jsonify
from flask_cors import cross_origin
from database import db
from werkzeug.utils import secure_filename
import os
import filetype
from utils.validations import validate_conf_img, validate_text_input, validate_email, validate_celular

app = Flask(__name__)

# Configuración de la carpeta de subida
UPLOAD_FOLDER = 'static/image'  # Carpeta donde se guardarán las imágenes
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegúrate de que la carpeta exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/' ,methods=['GET'])
def index():
    if request.method == 'GET':
        actividades = db.get_actividades()
        actividades = actividades[len(actividades) - 5:]
        actividades.reverse()
        data = []
        for actividad in actividades:
            comuna = db.get_comuna_by_id(actividad.comuna_id)
            foto = db.get_fotos_by_actividad_id(actividad.id)[0]
            tema = db.get_tema_by_actividad_id(actividad.id)
            data.append({
                'sector': actividad.sector,
                'fecha_inicio': actividad.dia_hora_inicio.date(),
                'hora_inicio': actividad.dia_hora_inicio.time().strftime('%H:%M'),
                'fecha_termino': actividad.dia_hora_termino.date(),
                'hora_termino': actividad.dia_hora_termino.time().strftime('%H:%M'),
                'tema': tema.tema if tema.tema != 'otro' else tema.glosa_otro,
                'comuna': comuna.nombre,
                'foto': foto.ruta_archivo
            })
        return render_template('index.html', data=data)

@app.route('/agregar-actividad', methods=['GET', 'POST'])
def agregar_actividad():
    if request.method == 'POST':
        comuna = request.form.get('comuna')
        sector = request.form.get('sector')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        redes = request.form.getlist('red-social')
        redes_sociales = []
        for red in redes:
            redes_sociales.append((red, request.form.get(red + "ID")))
        dia_hora_inicio = request.form.get('inicio')
        dia_hora_termino = request.form.get('termino')
        celular = request.form.get('celular')
        descripcion = request.form.get('descripcion')
        fotos = []
        ruta_fotos = []
        for i in range(0, 5):
            fotos.append(request.files.get('foto' + str(i + 1), ''))
        tema = request.form.get('tema')
        otroTema = request.form.get('inputOtroTema', '').strip()

        if not (validate_text_input(descripcion) and validate_text_input(nombre) and validate_text_input(sector) and validate_text_input(otroTema)):
            return render_template('agregar-actividad.html', error="Datos no válidos")
        
        if not validate_email(email):
            return render_template('agregar-actividad.html', error="Datos no válido")
        
        if celular:
            if not validate_celular(celular):
                return render_template('agregar-actividad.html', error="Datos no válidos")
        
        for red in redes_sociales:
            if not validate_text_input(red[1]):
                return render_template('agregar-actividad.html', error="Datos no válidos")
            
        new_filenames = []
        for foto in fotos:
            if foto and foto.filename != '':
                if not validate_conf_img(foto):
                    return render_template('agregar-actividad.html', error="Datos no válidos")
                else:
                    _filename = hashlib.sha256(
                        secure_filename(foto.filename) # nombre del archivo
                        .encode("utf-8") # encodear a bytes
                        ).hexdigest()
                    _extension = filetype.guess(foto).extension
                    img_filename = f"{_filename}.{_extension}"
                    new_filenames.append(img_filename)
                    foto.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                    ruta_archivo = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
                    ruta_relativa = ruta_archivo.replace('static/', '', 1)
                    ruta_fotos.append(ruta_relativa)
            
        db.create_actividad(
            comuna=comuna,
            sector=sector,
            nombre=nombre,
            email=email,
            celular=celular,
            dia_hora_inicio=dia_hora_inicio,
            dia_hora_termino=dia_hora_termino,
            descripcion=descripcion
        )
        actividad = db.get_actividades()[-1]  # Obtener la última actividad creada

        db.create_actividad_tema(
            tema=tema,
            glosa_otro=otroTema if tema == 'otro' else None,
            actividad_id=actividad.id
        )

        for nombre_archivo, ruta_archivo in zip(new_filenames, ruta_fotos):
            db.create_foto(
                ruta_archivo=ruta_archivo,
                nombre_archivo=nombre_archivo,
                actividad_id=actividad.id
            )

        for red_social in redes_sociales:
            db.create_contactar_por(
                nombre=red_social[0],
                identificador=red_social[1],
                actividad_id=actividad.id
            )
        return redirect(url_for('confirmacion'))
    elif request.method == 'GET':
        return render_template('agregar-actividad.html')

@app.route('/actividades', methods=['GET'])
def actividades():
    if request.method == 'GET':
        actividades = db.get_actividades()
        actividades.reverse()
        data = []
        for actividad in actividades:
            comuna = db.get_comuna_by_id(actividad.comuna_id)
            tema = db.get_tema_by_actividad_id(actividad.id)
            data.append({
                'actividad_id': actividad.id,
                'sector': actividad.sector,
                'fecha_inicio': actividad.dia_hora_inicio.date(),
                'hora_inicio': actividad.dia_hora_inicio.time().strftime('%H:%M'),
                'fecha_termino': actividad.dia_hora_termino.date(),
                'hora_termino': actividad.dia_hora_termino.time().strftime('%H:%M'),
                'nombre': actividad.nombre,
                'tema': tema.tema if tema.tema != 'otro' else tema.glosa_otro,
                'comuna': comuna.nombre,
                "fotos": len(db.get_fotos_by_actividad_id(actividad.id))
            })
        return render_template('lista-actividades.html', data=data)

@app.route('/actividades/<int:id>', methods=['GET', 'POST'])
def actividad(id):
    data = {}
    if request.method == 'GET':
        actividad = db.get_actividad_by_id(id)
        comuna = db.get_comuna_by_id(actividad.comuna_id)
        tema = db.get_tema_by_actividad_id(id)
        fotos = db.get_fotos_by_actividad_id(id)
        redes = db.get_redes_sociales_by_actividad_id(id)
        rutas_fotos = []
        for i in fotos:
            rutas_fotos.append(i.ruta_archivo)
        data = {
            'sector': actividad.sector,
            'fecha_inicio': actividad.dia_hora_inicio.date(),
            'hora_inicio': actividad.dia_hora_inicio.time().strftime('%H:%M'),
            'fecha_termino': actividad.dia_hora_termino.date(),
            'hora_termino': actividad.dia_hora_termino.time().strftime('%H:%M'),
            'nombre': actividad.nombre,
            'email': actividad.email,
            'celular': actividad.celular,
            'redes_sociales': redes,
            'comuna': comuna.nombre,
            'descripcion': actividad.descripcion,
            'tema': tema.tema if tema.tema != 'otro' else tema.glosa_otro,
            'fotos': rutas_fotos,
        }
        return render_template('actividad.html', data=data)
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        comentario = request.form.get('comentario')
        error = ""
        if not validate_text_input(nombre) or not validate_text_input(comentario):
            error = "Datos no válidos"
            return render_template("actividad.html", data=data, error=error)
        db.create_comentario(
            nombre=nombre,
            comentario=comentario,
            fecha=datetime.datetime.now(),
            actividad_id=id
        )
        return redirect(url_for('actividad', id=id))

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

@app.route('/get-stats-date', methods=['GET'])
@cross_origin(origins="127.0.0.1", supports_credentials=True)
def get_stats_dates():
    if request.method == 'GET':
        actividades = db.get_actividades()
        data = []
        for act in actividades:
            cantidad_de_actividades = len(db.get_actividades_by_date(act.dia_hora_inicio))
            data.append({
                'fecha': act.dia_hora_inicio.date().strftime('%Y-%m-%d'),
                'cantidad': cantidad_de_actividades
            })
        # quitar repetidos
        data = list({v['fecha']: v for v in data}.values())
        return jsonify(data)

@app.route('/get-stats-type', methods=['GET'])
@cross_origin(origins="127.0.0.1", supports_credentials=True)
def get_stats_type():
    if request.method == 'GET':
        actividades = db.get_actividades()
        data = [
            {"tema": "otro", "cantidad": 0},
            {"tema": "música", "cantidad": 0},
            {"tema": "deporte", "cantidad": 0},
            {"tema": "tecnología", "cantidad": 0},
            {"tema": "comida", "cantidad": 0},
            {"tema": "política", "cantidad": 0},
            {"tema": "ciencias", "cantidad": 0},
        ]
        for act in actividades:
            tema = db.get_tema_by_actividad_id(act.id)
            for t in data:
                if tema.tema == t['tema']:
                    t['cantidad'] += 1  
        return jsonify(data)

@app.route('/get-stats-activities', methods=['GET'])
@cross_origin(origins="127.0.0.1", supports_credentials=True)
def get_stats_activities():
    if request.method == 'GET':
        actividades = db.get_actividades()
        data = []
        months = range(1, 13)
        for month in months:
            cantidad_act_mañana = 0
            cantidad_act_tarde = 0
            cantidad_act_noche = 0
            for act in actividades:
                if act.dia_hora_inicio.month == month:
                    hora_inicio = act.dia_hora_inicio.time()
                    if hora_inicio < datetime.time(12, 0):
                        cantidad_act_mañana += 1
                    elif hora_inicio < datetime.time(18, 0):
                        cantidad_act_tarde += 1
                    else:
                        cantidad_act_noche += 1
            data.append({
                'mes': month,
                'cantidad_mañana': cantidad_act_mañana,
                'cantidad_tarde': cantidad_act_tarde,
                'cantidad_noche': cantidad_act_noche
            })
        return jsonify(data)

@app.route('/get-coments', methods=['GET'])
@cross_origin(origins="127.0.0.1", supports_credentials=True)
def get_coments():
    if request.method == 'GET':
        data = []
        comentarios = db.get_comentarios()
        for com in comentarios:
            actividad = db.get_actividad_by_id(com.actividad_id)
            data.append({
                'nombre': com.nombre,
                'texto': com.texto,
                'fecha': com.fecha.strftime('%Y-%m-%d %H:%M:%S'),
                'actividad_id': actividad.id,
            })
        return jsonify(data)

@app.route('/confirmacion')
def confirmacion():
    return render_template('confirmacion-agregar-tarea.html')

if __name__ == '__main__':
    app.run(debug=True)