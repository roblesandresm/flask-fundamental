from flask import Flask, render_template, request

app = Flask(__name__)

"""
@app.route('/')
def index():
    return 'Codigofacilito'
"""

# Se ejecuta anten de cualquier peticion al server
@app.before_request
def before_request():
    print('Antes de la peticion...')

# se ejecuta despues de una peticion al server
@app.after_request
def after_request(response):
    print('Despues de la peticion...')
    return response

def index():
    print('Estamos Realizando la peticion...')
    data = {
        'titulo': 'Home',
        'encabezado': 'Bienvenido(a) a mi sitio web',
        'contenido': 'Esta es mi primera pagina web como backend developer muchas mas.'
    }
    return render_template('index.html', data=data)


@app.route('/saludo/<nombre>')
def hola_mundo(nombre):
    return f'Hello {nombre}, how are you?'

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f'La suma es: {num1 + num2}'

@app.route('/lenguajes')
def lenguajes():
    data = {
        'titulo': 'Lenguajes',
        'encabezado': 'Lenguajes de programacion',
        'lenguajes': ['Python', 'Javascript', 'PHP', 'Golang', 'Java']
    }
    return render_template('lenguajes.html', data=data)

@app.route('/datos')
def datos():
    # print(request.args)
    if request.args.get('lenguaje'):
        lenguaje = request.args.get('lenguaje')
        return f'Tu lenguaje de programacion favorito es {lenguaje}'
    else:
        return 'No tienes un lenguaje de programacion favorito' 

@app.route('/contacto')
def contacto():
    data = {
        'titulo': 'Contacto',
        'encabezado': 'Bienvenido(a) a mi sitio web',
        'contenido': 'Esta es mi primera pagina web como backend developer muchas mas.'
    }
    return render_template('contacto.html', data=data)


if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=5005)
