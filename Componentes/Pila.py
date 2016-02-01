# -*- ENCODING: UTF-8 -*-
"""
 * File:   Pila.py
 * Author: Miguel Ochoa Hernandez
 *
"""

from Arbol.Nodo import *

__author__ = "Miguel Ochoa Hernandez"


class ElementoPila(object):

    """docstring for ElementoPila"""

    def __init__(self):
        super(ElementoPila, self).__init__()
        self.estado = 0
        self.nodo = None
        pass


class Terminal(ElementoPila):

    """docstring for Terminal"""

    def __init__(self, terminal):
        super(Terminal, self).__init__()
        self.terminal = terminal
        pass

    def imprimir(self):
        print("{ter}".format(ter=self.terminal), end="")
        pass


class NoTerminal(ElementoPila):

    """docstring for NoTerminal"""

    def __init__(self, no_terminal, reduccion, estado):
        super(NoTerminal, self).__init__()
        self.estado = estado
        self.reduccion = reduccion
        self.no_terminal = no_terminal
        pass

    def imprimir(self):
        print("{nt}".format(nt=self.no_terminal), end="")
        pass


class Estado(ElementoPila):

    """docstring for Estado"""

    def __init__(self, estado):
        super(Estado, self).__init__()
        self.estado = estado
        pass

    def imprimir(self):
        print("{est}".format(est=self.estado), end="")
        pass
