#!/usr/bin/env python

from clases import triangulos, rectangulos, cuadrados, rombos, pentagonos

from clases.figuras import Figura

from clases.triangulos import Triangulo
from clases.rectangulos import Rectangulo
from clases.cuadrados import Cuadrado
from clases.pentagonos import Pentagono
from clases.rombos import Rombo

import argparse

__author__ = 'REBECA GONZÁLEZ BALADO'


# **** PARSER **** #
# creamos el parser
parser = argparse.ArgumentParser(description='Calculadora de área y perímetro de figuras // [area]/[per]imetro // '
                                             '[t]riángulo/[r]ectángulo/[c]uadrado/[p]entágono/r[o]mbo) // '
                                             'valores [1~3]')

# sintaxis: python figurasPrincipal.py -o 'operacion' -f 'figura' -v 'valores'

# añadimos los argumentos
parser.add_argument('-o', '--operacion', type=str, choices=['area', 'per'], help='Operación')
parser.add_argument('-f', '--figura', type=str, choices=['t', 'r', 'c', 'p', 'o'],
                    help='Tipo de figura')
parser.add_argument('-v', '--valores', type=float, nargs='+', help='Valor')

# parseamos los argumentos
args = parser.parse_args()
variables = vars(args)

# buscamos el tipo de operacion en el enum
operacion = args.operacion
if operacion == 'area':
    operacion = Figura.Operacion.AREA
else:
    operacion = Figura.Operacion.PERIMETRO

# pasamos los numeros negativos a positivos
if args.valores is not None:
    valores = [abs(valor) for valor in args.valores]

# lista de figuras consultadas
listaFiguras = []


# **** METODOS **** #
# peticion de numeros
def peticionnumerica():
    while True:
        try:
            num = float(input())
            if num > 0:
                break
            else:
                print('Introduce un número válido.')
        except ValueError:
            print('Introduce sólo números.')

    return num


# historial de figuras consultadas
def historial():
    if len(listaFiguras) > 0:
        for figura in listaFiguras:
            figura.datosfigura()
    else:
        print('El historial está vacio.')


# instanciamos un triangulo
def creartriangulo(consola):
    if consola:
        triangulo = triangulos.Triangulo(valores[0], valores[1], valores[2])
        triangulo.tostr(operacion)

    else:
        listavalores = []

        for i in range(0, len(Triangulo.nombresvalores)):
            print(f'Introduzca el valor del {Triangulo.nombresvalores[i]}:')
            listavalores.append(peticionnumerica())

        triangulo = triangulos.Triangulo(listavalores[0], listavalores[1], listavalores[2])
        triangulo.tostr(Figura.Operacion.AREA)
        triangulo.tostr(Figura.Operacion.PERIMETRO)
        listaFiguras.append(triangulo)


# instanciamos un rectangulo
def crearrectangulo(consola):
    if consola:
        rectangulo = rectangulos.Rectangulo(valores[0], valores[1])
        rectangulo.tostr(operacion)

    else:
        listavalores = []

        for i in range(0, len(Rectangulo.nombresvalores)):
            print(f'Introduzca el valor de la {Rectangulo.nombresvalores[i]}:')
            listavalores.append(peticionnumerica())

        rectangulo = rectangulos.Rectangulo(listavalores[0], listavalores[1])
        rectangulo.tostr(Figura.Operacion.AREA)
        rectangulo.tostr(Figura.Operacion.PERIMETRO)
        listaFiguras.append(rectangulo)


# instanciamos un cuadrado
def crearcuadrado(consola):
    if consola:
        cuadrado = cuadrados.Cuadrado(valores[0])
        cuadrado.tostr(operacion)

    else:
        print(f'Introduzca el valor del {Cuadrado.nombresvalores[0]}: ')
        valor = peticionnumerica()

        cuadrado = cuadrados.Cuadrado(valor)
        cuadrado.tostr(Figura.Operacion.AREA)
        cuadrado.tostr(Figura.Operacion.PERIMETRO)
        listaFiguras.append(cuadrado)


# instanciamos un pentagono
def crearpentagono(consola):
    if consola:
        pentagono = pentagonos.Pentagono(valores[0], valores[1])
        pentagono.tostr(operacion)

    else:
        listavalores = []

        for i in range(0, len(Pentagono.nombresvalores)):
            print(f'Introduzca el valor del {Pentagono.nombresvalores[i]}:')
            listavalores.append(peticionnumerica())

        pentagono = pentagonos.Pentagono(listavalores[0], listavalores[1])
        pentagono.tostr(Figura.Operacion.AREA)
        pentagono.tostr(Figura.Operacion.PERIMETRO)
        listaFiguras.append(pentagono)


# instanciamos un rombo
def crearrombo(consola):
    if consola:
        rombo = rombos.Rombo(valores[0], valores[1])
        rombo.tostr(operacion)

    else:
        print(f'Introduzca el valor del {Rombo.nombresvalores[0]}: ')
        valor1 = peticionnumerica()

        print(f'Introduzca el valor de la {Rombo.nombresvalores[1]}: ')
        valor2 = peticionnumerica()

        rombo = rombos.Rombo(valor1, valor2)
        rombo.tostr(Figura.Operacion.AREA)
        rombo.tostr(Figura.Operacion.PERIMETRO)
        listaFiguras.append(rombo)


# ***** MENUS ***** #
# menu selector para ejecucion por consola
def menuconsola():
    # imprimimos los parametros introducidos
    print(variables)

    figura = args.figura

    # selector menu
    if figura == 't':
        print('\nTriángulo')

        if len(valores) >= len(Triangulo.nombresvalores):
            creartriangulo(True)
        else:
            print(f'Número insuficiente de parámetros. Requeridos [{len(Triangulo.nombresvalores)}].\n')

    elif figura == 'r':
        print('\nRectángulo')

        if len(valores) >= len(Rectangulo.nombresvalores):
            crearrectangulo(True)
        else:
            print(f'Número insuficiente de parámetros. Requeridos [{len(Rectangulo.nombresvalores)}].\n')

    elif figura == 'c':
        print('\nCuadrado')
        crearcuadrado(True)

    elif figura == 'p':
        print('\nPentágono')

        if len(valores) >= len(Pentagono.nombresvalores):
            crearpentagono(True)
        else:
            print(f'Número insuficiente de parámetros. Requeridos [{len(Pentagono.nombresvalores)}].\n')

    elif figura == 'o':
        print('\nRombo')

        if len(valores) >= len(Rombo.nombresvalores):
            crearrombo(True)
        else:
            print(f'Número insuficiente de parámetros. Requeridos [{len(Rombo.nombresvalores)}].\n')

    else:
        print('Elige una opción válida.')


# menu selector
def menu():
    while True:
        print('\nCalculadora geométrica (área y perímetro)')
        print('T - Triángulo')
        print('R - Rectángulo')
        print('C - Cuadrado')
        print('P - Pentágono')
        print('O - Rombo')
        print('H - Historial')
        print('X - Salir')
        opcion = str(input('\nSeleccione una figura: '))

        # selector menu
        if opcion.casefold() == 't':
            print('\nTriángulo')
            creartriangulo(False)
        elif opcion.casefold() == 'r':
            print('\nRectángulo')
            crearrectangulo(False)
        elif opcion.casefold() == 'c':
            print('\nCuadrado')
            crearcuadrado(False)
        elif opcion.casefold() == 'p':
            print('\nPentágono')
            crearpentagono(False)
        elif opcion.casefold() == 'o':
            print('\nRombo')
            crearrombo(False)
        elif opcion.casefold() == 'h':
            print('\nHistorial')
            historial()
        elif opcion.casefold() == 'x':
            break
        else:
            print('Elige una opción válida.')


# seleccion de menus
def main():
    if args.figura is not None and args.operacion is not None and args.valores is not None:
        menuconsola()
    else:
        menu()


if __name__ == '__main__':
    main()
