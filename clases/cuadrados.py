from clases.cuadrilateros import Cuadrilatero


class Cuadrado(Cuadrilatero):
    nombrefigura = 'cuadrado'
    nombresvalores = ['lado']

    # constructor
    def __init__(self, lado):
        valores = [lado]
        super(Cuadrado, self).__init__(valores, lado, lado)
