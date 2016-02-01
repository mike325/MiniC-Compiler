# -*- ENCODING: UTF-8 -*-
"""
 * File:   Semantico.py
 * Author: Miguel Ochoa Hernandez
 * C0digo: 212355068
 * Taller de compiladores
 *
"""

from __future__ import print_function
from  Componentes import  Globales

__author__ = "Miguel Ochoa Hernandez"


class Semantico(object):

    """Analizador Semantico"""

    def __init__(self):
        self.arbol = None
        # self.tablaSimbolos = None
        pass

    def analizar(self, arbol):
        Globales.reiniciar()
        self.arbol = arbol
        self.arbol.decideTipo()
        # self.tablaSimbolos.muestra()
        # self.muestraErrores()
        pass

    def muestraErrores(self):
        pass
