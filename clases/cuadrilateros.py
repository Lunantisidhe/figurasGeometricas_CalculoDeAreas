from clases.figuras import Figura


class Cuadrilatero (Figura):
    nombrefigura = 'cuadrilátero'
    nombresvalores = []

    # constructor
    def __init__(self, valores, valor1, valor2):
        super(Cuadrilatero, self).__init__(valores)

        self.v1 = valor1
        self.v2 = valor2

    # calculo del area de un cuadrilatero a partir de sus valores
    def area(self):
        return [self.v1 * self.v2]

    # calculo del perimetro de un cuadrilatero a partir de sus valores
    def perimetro(self):
        return [2 * (self.v1 + self.v2)]
