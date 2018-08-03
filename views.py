from flask import request, redirect, render_template, url_for
##from app import app
from py_expression_eval import Parser
from app import secante

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/resolve', methods=['POST'])
def resolve():

    if request.method == 'POST':
        secante.texto = request.form.get('fx')
        secante.x0 = float(request.form.get('x0'))
        secante.x1 = float(request.form.get('x1'))
        parser = Parser()
        secante.tol = parser.parse(request.form.get('tol')).evaluate({})
        secante.n = int(request.form.get('iteracion'))

        result, results = secante.Secante(secante.x0, secante.x1, secante.tol, secante.n, secante.f)
        newfx = secante.texto.replace('*','')
        return render_template(
            'resolve.html', result=result, fx=newfx, results=results
        )
    else:
        error = 'Oopss! ... Algo salio Mal'
        return render_template('index.html', error=error)

