#!/usr/bin/env python

# -*- ENCODING: UTF-8 -*-
"""
 * File:   main.py
 * Author: Miguel Ochoa Hernandez
 * Codigo: 212355068
 * Taller de compiladores
 *
"""

import argparse
import sys
import os

from Componentes.Sintactico import Sintactico
from Componentes.Semantico import Semantico
from Componentes.Excepciones import Errores
from Componentes import Globales
from Componentes.Leer import Leer

__author__ = "Miguel Ochoa Hernandez"


def _parseArgs():
    """ Parse CLI arguments
    :returns: argparse.ArgumentParser class instance

    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--version',
                        dest='show_version',
                        action='store_true',
                        help='print script version and exit')

    parser.add_argument('-l',
                        '--logging',
                        dest='logging',
                        default="INFO",
                        type=str,
                        help='Enable debug messages')

    parser.add_argument('-f',
                        '--file',
                        dest='file',
                        type=str,
                        help='File to analyze')

    return parser.parse_args()


def main():
    """
    Main function
    """
    errors = 0
    filename = None

    try:
        if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
            filename = sys.argv[1]
        else:
            args = _parseArgs()
            filename = args.file if args.file is not None and len(args.file) > 0 else None

        lectura = Leer()

        if filename is None:
            filename = lectura.pedirArchivo()

        inicio = Sintactico()
        arbol = inicio.entrada(filename)

        if arbol is not None:
            semantico = Semantico()
            semantico.analizar(arbol)
            funcion, _ = Globales.tabla_simbolos.buscaFuncion("main")
            if funcion is None:
                raise Errores("No se declaro la funcion main")

            print("Cadena aceptada")
            with open("ensamblador.asm", "w") as archivo:
                codigo = semantico.arbol.generacionCodigo()
                archivo.write(codigo)
    except KeyboardInterrupt:
        errors = 1
    except Errores as e:
        # Globales.totalAmbitos()
        Globales.totalIdentificadores()
        print("\n{0}".format(e))
        errors = 2
    return errors


if __name__ == '__main__':
    exit(main())
