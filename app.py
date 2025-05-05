from flask import Flask, redirect, render_template, request, url_for

from database import db

app = Flask(__name__)

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
        foto = request.form.get('foto')
        tema = request.form.get('tema')
        otroTema = request.form.get('inputOtroTema')
        db.create_actividad(comuna, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion)
        db.create_foto(foto, tema, otroTema)
        db.create_actividad_tema(tema, otroTema, db.get)
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