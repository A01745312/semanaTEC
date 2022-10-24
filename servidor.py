from flask import Flask, request, jsonfify, render_template


# Generar servidor (Back-end)

servidorWeb = Flask(__name__)

# Anotacion

@servidorWeb.route("/test", methods = ['GET'])


def formulario ():
    return render_template('pagina.html')


if __name__ == '__main__':
    servidorWeb.run(debug = False, host = '0.0.0.0', port = '8080')