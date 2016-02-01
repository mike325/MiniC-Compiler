# -*- ENCODING: UTF-8 -*-
"""
 * File:   main.py
 * Author: Miguel Ochoa Hernandez
 * Codigo: 212355068
 * Taller de compiladores
 *
"""

from Componentes.Sintactico import *
from Componentes.Semantico import *
from Componentes.Excepciones import *

__author__ = "Miguel Ochoa Hernandez"


def main():
    inicio = Sintactico()
    # inicio.entrada()
    arbol = inicio.entrada()

    if not(arbol is None):
        try:
            semantico = Semantico()
            semantico.analizar(arbol)
            funcion, pos = Globales.tabla_simbolos.buscaFuncion("main")
            if funcion is None:
                raise Errores("No se declaro la funcion main")
                pass

            print("Cadena aceptada")
            with open("ensamblador.asm", "w") as archivo:
                codigo = semantico.arbol.generacionCodigo()
                archivo.write(codigo)
                pass
            pass
        except Errores as e:
            # Globales.totalAmbitos()
            Globales.totalIdentificadores()
            print("\n{0}".format(e))
            pass
        pass
    pass

if __name__ == '__main__':
    main()
