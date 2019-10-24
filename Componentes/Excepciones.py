# -*- ENCODING: UTF-8 -*-
"""
 * File:   TablaSimbolos.py
 * Author: Miguel Ochoa Hernandez
 * C0digo: 212355068
 * Taller de compiladores
 *
"""

from __future__ import print_function


__author__ = "Miguel Ochoa Hernandez"


class Errores(Exception):

    def __init__(self, code):
        self.code = "Error Semantico, {0}".format(code)

    def __str__(self):
        return repr(self.code)
