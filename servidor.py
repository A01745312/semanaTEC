from crypt import methods
from fileinput import filename
from unittest import result

from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from joblib import load
import numpy as np
import os

# Cargar el modelo
dt = load('modelo.joblib')


# Generar servidor (Back-end)
servidorWeb = Flask(__name__)

# --------------------  RUTAS  -------------------- #

# Anotacion
@servidorWeb.route("/test", methods = ['GET'])
def formulario ():
    return render_template('pagina.html')

# *****  modeloIA  *****

# Procesar datos a traves del form
@servidorWeb.route("/modeloIA", methods = ['POST'])
def modeloForm ():
    # Procesar datos de entrada
    contenido = request.form
    print(contenido)

    datosEntrada = np.array([
        7.4000,0.6800,0.1600,1.8000,0.0780,12.0000,39.0000,0.9977,
        contenido['pH'],
        contenido['sulfatos'],
        contenido['alcohol']
    ])

    # Utilizar el modelo
    resultado = dt.predict(datosEntrada.reshape(1, -1))

<<<<<<< HEAD
    return jsonify({"Resultado": "datos recibidos"})
=======

    return jsonify({"Resultado": str(resultado[0])})
>>>>>>> parent of 55b4f17 (pruebaRes)

# *****  modeloFile  *****

# Procesar datos de un archivo
@servidorWeb.route("/modeloFile", methods = ['POST'])
def modeloFile ():
    # Procesar datos de entrada
    f = request.files['file']
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd(), filename)
    f.save(path)
    file = open(path,'r')
    for line in file:
        print(line)
    return jsonify({"Resultado": "datos recibidos"})

# *****  modelo  *****

@servidorWeb.route('/modelo', methods = ["POST"])
def model():
    contenido = request.json
    print(contenido)
    return jsonify({"Resultado": "datos recibidos"})

# ----------------------------------------------------- #

if __name__ == '__main__':
    servidorWeb.run(debug = False, host = '0.0.0.0', port = '8080')