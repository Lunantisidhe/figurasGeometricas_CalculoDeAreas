import math
from clases.figuras import Figura


class Triangulo(Figura):
    nombrefigura = 'triángulo'
    nombresvalores = ['lado A', 'lado B', 'lado C']

    # constructor
    def __init__(self, ladoa, ladob, ladoc):
        valores = [ladoa, ladob, ladoc]
        super(Triangulo, self).__init__(valores)

        self.a = ladoa
        self.b = ladob
        self.c = ladoc

    # calculo del area de un triangulo a partir de sus lados
    def area(self):
        return [(math.sqrt((self.a + self.b - self.c) * (self.a - self.b + self.c) * (-self.a + self.b + self.c)
                           * (self.a + self.b + self.c))) / 4]

    # calculo del perimetro de un triangulo a partir de sus lados
    def perimetro(self):
        return [self.a + self.b + self.c]

    # comprobamos que el triangulo introducido es posible
    def comprobar_triangulo(self, impresion):
        numeros = sorted([self.a, self.b, self.c])
        if (numeros[0] + numeros[1]) < numeros[2]:
            if impresion:
                print(f'El triángulo introducido es imposible ya que {numeros[0]:.3f} + {numeros[1]:.3f} '
                      f'< {numeros[2]:.3f}.\n')
            return False
        return True

    # comprobamos que sea un triangulo posible antes de realizar la impresion
    def tostr(self, operacion):
        if self.comprobar_triangulo(True):
            Figura.tostr(self, operacion)

    # comprobamos que sea un triangulo posible antes de realizar la impresion
    def datosfigura(self):
        if self.comprobar_triangulo(False):
            Figura.datosfigura(self)
        else:
            print(f'{self.nombrefigura.capitalize()}[{self.nombresvalores[0]}: {self.valores[0]:.3f}, '
                  f'{self.nombresvalores[1]}: {self.valores[1]:.3f}, {self.nombresvalores[2]}: {self.valores[2]:.3f}, '
                  f'área: [-], perímetro: [-], TRIÁNGULO IMPOSIBLE]')
