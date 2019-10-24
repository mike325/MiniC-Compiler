# -*- ENCODING: UTF-8 -*-
"""
 * File:   Leer.py
 * Author: Miguel Ochoa Hernandez
 * Código: 212355068
 * Taller de compiladores
 *
"""

from __future__ import print_function

# from Componentes.Lexico import *

__author__ = "Miguel Ochoa Hernandez"


class Leer():
    """Clase para leer y procesar un archivo"""

    def __init__(self):
        super(Leer, self).__init__()

    def pedirArchivo(self):
        correcto = False
        while not correcto:
            try:
                print("\nArchivo a analisar: ", end="")
                nombre = input()
                archivo = open(nombre, "r")
                archivo.close()
                correcto = True
            except IOError:
                print("No se ingreso el archivo correcto")
        print()
        return nombre
