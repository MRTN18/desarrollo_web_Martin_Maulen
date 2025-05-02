from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/' ,methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/agregar-actividad')
def agregar_actividad():
    return render_template('agregar-actividad.html')

@app.route('/actividades')
def actividades():
    return render_template('lista-actividades.html')

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')