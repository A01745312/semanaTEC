from crypt import methods
from fileinput import filename

from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from joblib import load
import numpy as np
import os


# Generar servidor (Back-end)

servidorWeb = Flask(__name__)

# Anotacion
@servidorWeb.route("/test", methods = ['GET'])
def formulario ():
    return render_template('pagina.html')

# Procesar datos a traves del form
@servidorWeb.route("/modeloIA", methods = ['POST'])
def modeloForm ():
    # Procesar datos de entrada
    contenido = request.form
    print(contenido)

    return jsonify({"Resultado": "datos recibidos"})


# Procesar datos de un archivo
@servidorWeb.route("/modeloFile", methods = ['POST'])
def modeloFile ():
    # Procesar datos de entrada
    f = request.files['file']
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd(), 'files', filename)
    f.save(path)
    file = open(path,'r')
    for line in file:
        print(line)
    return jsonify({"Resultado": "datos recibidos"})


if __name__ == '__main__':
    servidorWeb.run(debug = False, host = '0.0.0.0', port = '8080')