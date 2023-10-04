from clases.cuadrilateros import Cuadrilatero


class Rombo (Cuadrilatero):
    nombrefigura = 'rombo'
    nombresvalores = ['lado', 'altura']

    # constructor
    def __init__(self, lado, altura):
        valores = [lado, altura]
        super(Rombo, self).__init__(valores, lado, altura)
