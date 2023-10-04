from enum import Enum


class Figura:
    nombrefigura = 'figura'
    nombresvalores = []

    # constructor
    def __init__(self, valores):
        self.valores = valores

    def area(self):
        return [0]

    def perimetro(self):
        return [0]

    class Operacion(Enum):
        AREA = 1
        PERIMETRO = 2

    # impresion area y perimetro
    def tostr(self, operacion):

        # impresion area
        if operacion == self.Operacion.AREA:
            area = [round(n, 3) for n in self.area()]

            print(f'El área del {self.nombrefigura} de ', end='')
            if len(self.valores) == 1:
                print(f'{self.nombresvalores[0]} {self.valores[0]:.3f} unidades ', end='')
            elif len(self.valores) == 2:
                print(f'{self.nombresvalores[0]} {self.valores[0]:.3f} unidades y {self.nombresvalores[1]} '
                      f'{self.valores[1]:.3f} unidades ', end='')
            else:
                print(f'{self.nombresvalores[0]} {self.valores[0]:.3f} unidades, {self.nombresvalores[1]} '
                      f'{self.valores[1]:.3f} unidades y {self.nombresvalores[2]} {self.valores[2]:.3f} unidades ', end='')
            print(f'es de {area} unidades.\n')

        # impresion perimetro
        elif operacion == self.Operacion.PERIMETRO:
            perimetro = [round(n, 3) for n in self.perimetro()]

            print(f'El perímetro del {self.nombrefigura} de ', end='')
            if len(self.valores) == 1:
                print(f'{self.nombresvalores[0]} {self.valores[0]:.3f} ', end='')
            elif len(self.valores) == 2:
                print(f'{self.nombresvalores[0]} {self.valores[0]:.3f} unidades y {self.nombresvalores[1]} '
                      f'{self.valores[1]:.3f} unidades ', end='')
            else:
                print(f'{self.nombresvalores[0]} {self.valores[0]:.3f} unidades, {self.nombresvalores[1]} '
                      f'{self.valores[1]:.3f} unidades y {self.nombresvalores[2]} {self.valores[2]:.3f} unidades ', end='')
            print(f'es de {perimetro} unidades.\n')

        else:
            return 0

    # datos de la figura para impresion del historial
    def datosfigura(self):
        area = [round(n, 3) for n in self.area()]
        perimetro = [round(n, 3) for n in self.perimetro()]

        print(f'{self.nombrefigura.capitalize()}[', end='')

        for i in range(0, len(self.nombresvalores)):
            print(f'{self.nombresvalores[i]}: {self.valores[i]:.3f}, ', end='')

        if len(self.area()) > 1:
            print(f'áreas posibles: {area}, perímetros posibles: {perimetro}')
        else:
            print(f'área: {area}, perímetro: {perimetro}]')
