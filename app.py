from flask import Flask, render_template, request

from database import db

app = Flask(__name__)

@app.route('/' ,methods=['GET'])
def index():
    if request.method == 'GET':
        actividades = db.get_actividades()[:5]
        data = []
        for actividad in actividades:
            comuna = db.get_comuna_by_id(actividad.comuna_id)
            data.append({
                'sector': actividad.sector,
                'dia_hora_inicio': actividad.dia_hora_inicio,
                'dia_hora_termino': actividad.dia_hora_termino,
                'descripcion': actividad.descripcion,
                'comuna': comuna.nombre,
            })
        return render_template('index.html', data=data)

@app.route('/agregar-actividad')
def agregar_actividad():
    return render_template('agregar-actividad.html')

@app.route('/actividades')
def actividades():
    return render_template('lista-actividades.html')

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')