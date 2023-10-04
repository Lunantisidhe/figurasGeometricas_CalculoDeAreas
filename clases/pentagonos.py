import math
from clases.figuras import Figura


class Pentagono (Figura):
    nombrefigura = 'pentágono'
    nombresvalores = ['lado', 'apotema']

    # constructor
    def __init__(self, lado, apotema):
        valores = [lado, apotema]
        super(Pentagono, self).__init__(valores)

        self.la = lado
        self.a = apotema

    # calculo del area de un pentagono a partir de su lado y apotema
    def area(self):
        # si es un pentagono regular, calculamos su area
        if not self.comprobarapotema(False):
            return [5 * self.la * self.a * 0.5]

        # si no es regular, calculamos su area con el lado y apotema corregidos
        else:
            apotemacorrecto = self.comprobarapotema(False)[0]
            ladocorrecto = self.comprobarapotema(False)[1]

            # damos las dos posibles areas correctas
            return [(5 * self.la * apotemacorrecto * 0.5), (5 * ladocorrecto * self.a * 0.5)]

    # calculo del perimetro de un pentagono a partir de su lado y apotema
    def perimetro(self):
        # si es un pentagono regular, calculamos su perimetro
        if not self.comprobarapotema(False):
            return [5 * self.la]

        # si no es regular, calculamos su perimetro con el lado y apotema corregidos
        else:
            ladocorrecto = self.comprobarapotema(False)[1]

            # damos los dos posibles perimetros correctos
            return [(5 * self.la), (5 * ladocorrecto)]

    # comprobamos que la apotema introducida es correcta
    def comprobarapotema(self, impresion):
        apotemacorrecto = self.la / (2 * math.sqrt(5 - (2 * math.sqrt(5))))
        ladocorrecto = 2 * self.a * math.sqrt(5 - 2 * math.sqrt(5))

        if self.a != apotemacorrecto and self.la != ladocorrecto:
            if impresion:
                print('El pentágono introducido no es regular.\n')

                # damos los datos del pentagono regular con lado introducido
                print(f'De ser un pentágono regular de lado {self.la :.3f} tendría un apotema '
                      f'igual a {apotemacorrecto:.3f}.')

                # damos los datos del pentagono regular con apotema introducida
                print(f'De ser un pentágono regular de apotema {self.a :.3f}, tendría un lado '
                      f'igual a {ladocorrecto:.3f}.\n')

            return [apotemacorrecto, ladocorrecto]
        return False

    # impresion de pentagonos
    def tostr(self, operacion):
        if not self.comprobarapotema(True):
            Figura.tostr(self, operacion)
        else:
            # guardamos los datos originales para poder recuperarlos
            aog = self.a
            log = self.la

            # damos los datos del pentagono regular con lado introducido
            apotemacorrecto = self.comprobarapotema(False)[0]
            self.a = apotemacorrecto
            self.valores[1] = apotemacorrecto

            Figura.tostr(self, operacion)

            # reseteamos el apotema
            self.a = aog
            self.valores[1] = aog

            # damos los datos del pentagono regular con apotema introducida
            ladocorrecto = self.comprobarapotema(False)[1]
            self.la = ladocorrecto
            self.valores[0] = ladocorrecto

            Figura.tostr(self, operacion)

            # reseteamos el lado
            self.la = log
            self.valores[0] = log
