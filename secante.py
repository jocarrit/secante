''' Metodo de la Secante para encontar la raiz de una funcion
    x= x1-f(x1)*(x1-x0)/(f(x1)-f(x0)). Entrada de datos: xo, x1,
    tolerancia,numero de iteraciones maximo y funcion
'''


from py_expression_eval import Parser

texto = 'x'
x0 = 0
x1 = 0
tol = 0
n = 0


def Secante(x0, x1, tol, n, f):
    lista = []
    i = 1
    while i <= n:
        x = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))

        lista.append(x)
        if abs(x - x1) < tol:
            return x, lista
        i = i + 1
        x0 = x1  # redefinir x0
        x1 = x  # redefinir x1

    print('El metodo fracaso despues de %d iteraciones' % N)


def f(num):
    parser2 = Parser()
    formula = parser2.parse(texto).evaluate({'x': num})
    return formula







