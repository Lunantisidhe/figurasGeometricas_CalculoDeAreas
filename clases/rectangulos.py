from clases.cuadrilateros import Cuadrilatero


class Rectangulo (Cuadrilatero):
    nombrefigura = 'rectángulo'
    nombresvalores = ['base', 'altura']

    # constructor
    def __init__(self, base, altura):
        valores = [base, altura]
        super(Rectangulo, self).__init__(valores, base, altura)
