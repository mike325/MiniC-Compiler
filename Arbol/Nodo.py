# -*- ENCODING: UTF-8 -*-
"""
 * File:   Nodo.py
 * Author: Miguel Ochoa Hernandez
 *
"""

__author__ = "Miguel Ochoa Hernandez"


class Nodo(object):

    """docstring for Nodo"""

    def __init__(self):
        super(Nodo, self).__init__()
        self.simbolo = None
        self.siguiente = None
        self.tipo_dato = None
        self.tabla_simbolos = None
        self.ambito = None

    def inicializar(self, pila):
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        pass

    # Pendiente
    def decideTipo(self):
        pass

    def generacionCodigo(self):
        print("Nodo.generaCodigo")
        return ""


class Expresion(Nodo):

    """docstring for Expresion"""

    def __init__(self):
        super(Expresion, self).__init__()
        self.izquierdo = None
        self.derecha = None
        self.expresion = None
        self.termino = None

    def inicializar(self, pila):
        self.siguiente = pila.pop().nodo
        return pila

    def multiExpresion(self, pila):
        pila.pop()
        pila.pop()
        pila.pop()

        self.expresion = pila.pop().nodo

        pila.pop()
        pila.pop()
        return pila

    def definicionTermino(self, pila):
        pila.pop()
        self.termino = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Expresion>".format(tabulaciones))
        if not(self.expresion is None):
            self.expresion.imprimir(tabulaciones + "\t")
        else:
            self.termino.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        if not(self.expresion is None):
            self.expresion.validarTipo()
            if self.expresion.tipo_dato != "e":
                self.tipo_dato = self.expresion.tipo_dato
        else:
            self.termino.validarTipo()
            if self.termino.tipo_dato != "e":
                self.tipo_dato = self.termino.tipo_dato

    def regresaSimbolo(self):
        return ""
