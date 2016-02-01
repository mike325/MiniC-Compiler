# -*- ENCODING: UTF-8 -*-
"""
 * File:   Lexico.py
 * Author: Miguel Ochoa Hernandez
 * C0digo: 212355068
 * Taller de compiladores
 *
"""

from __future__ import print_function

__author__ = "Miguel Ochoa Hernandez"


class Lexico(object):

    """Analizador Lexico"""

    def __init__(self):
        super(Lexico, self).__init__()
        self.estado = 0
        self.simbolo = ""
        self.tipo = 0
        self.index = 0
        self.error = False
        self.estados_aceptados = {2: self.tipoReservado}
        self.estados_aceptados[1] = 0
        self.estados_aceptados[3] = 1
        self.estados_aceptados[5] = 2
        self.estados_aceptados[8] = 3
        self.estados_aceptados[9] = 12
        self.estados_aceptados[10] = 13
        self.estados_aceptados[11] = 5
        self.estados_aceptados[12] = 6
        self.estados_aceptados[13] = self.dividir
        self.estados_aceptados[14] = self.dividir
        self.estados_aceptados[15] = self.dividir
        self.estados_aceptados[16] = 18
        self.estados_aceptados[17] = 10
        self.estados_aceptados[18] = 11
        self.estados_aceptados[19] = 7
        self.estados_aceptados[20] = 7
        self.estados_aceptados[22] = 8
        self.estados_aceptados[24] = 9
        self.estados_aceptados[25] = 23
        pass

    def siguienteEstado(self, linea, estado):
        self.estado = estado
        self.simbolo = self.simbolo + linea[self.index]
        self.index = self.index + 1
        pass

    def espacios(self, linea):
        while linea[self.index] == " " or linea[self.index] == "\t" or linea[self.index] == "\n" or linea[self.index] == "\r":
            self.index = self.index + 1
            pass
        linea = linea[self.index:]
        return linea
        pass

    def reservada(self):
        es_reservada = True
        if self.simbolo == "int" or self.simbolo == "float" or self.simbolo == "void":
            self.estado = 2
            pass
        elif self.simbolo == "if" or self.simbolo == "else" or self.simbolo == "while":
            self.estado = 2
            pass
        elif self.simbolo == "return":
            self.estado = 2
            pass
        else:
            es_reservada = False
            pass
        return es_reservada
        pass

    def identificador(self, linea):
        if linea[self.index].isalpha() or linea[self.index] == "_":
            self.siguienteEstado(linea, 1)
            if not self.reservada():
                self.identificador(linea)
                pass
            pass
        elif linea[self.index].isdigit():
            self.siguienteEstado(linea, 1)
            self.identificador(linea)
            pass
        pass

    def real(self, linea):
        if linea[self.index].isdigit():
            self.siguienteEstado(linea, 5)
            self.real(linea)
            pass
        pass

    def entero(self, linea):
        if linea[self.index].isdigit():
            self.siguienteEstado(linea, 3)
            self.entero(linea)
            pass
        elif linea[self.index] == ".":
            self.siguienteEstado(linea, 4)
            self.real(linea)
            pass
        pass

    def cadena(self, linea):
        if linea[self.index] != "\"":
            self.siguienteEstado(linea, 7)
            self.cadena(linea)
            pass
        pass

    def dependeSiguiente(self, caracter, linea, estado):
        if linea[self.index] == caracter:
            self.siguienteEstado(linea, estado)
            pass
        pass

    def analizar(self, linea):
        try:
            # ******* Recursivos *******
            if linea[self.index].isalpha() or linea[self.index] == "_":
                self.siguienteEstado(linea, 1)
                self.identificador(linea)
                pass
            elif linea[self.index].isdigit():
                self.siguienteEstado(linea, 3)
                self.entero(linea)
                pass
            elif linea[self.index] == "\"":
                self.siguienteEstado(linea, 6)
                self.cadena(linea)
                if linea[self.index] == "\"":
                    self.siguienteEstado(linea, 8)
                    pass
                pass
            # ******* Aceptacion directa *******
            elif linea[self.index] == ";":
                self.siguienteEstado(linea, 9)
                pass
            elif linea[self.index] == ",":
                self.siguienteEstado(linea, 10)
                pass
            elif linea[self.index] == "+" or linea[self.index] == "-":
                self.siguienteEstado(linea, 11)
                pass
            elif linea[self.index] == "*" or linea[self.index] == "/":
                self.siguienteEstado(linea, 12)
                pass
            elif linea[self.index] == "(" or linea[self.index] == ")":
                self.siguienteEstado(linea, 13)
                pass
            elif linea[self.index] == "[" or linea[self.index] == "]":
                self.siguienteEstado(linea, 14)
                pass
            elif linea[self.index] == "{" or linea[self.index] == "}":
                self.siguienteEstado(linea, 15)
                pass
            # ******* Aceptacion parcial *******
            elif linea[self.index] == "=":
                self.siguienteEstado(linea, 16)
                self.dependeSiguiente("=", linea, 18)
                pass
            elif linea[self.index] == "!":
                self.siguienteEstado(linea, 17)
                self.dependeSiguiente("=", linea, 18)
                pass
            elif linea[self.index] == "<" or linea[self.index] == ">":
                self.siguienteEstado(linea, 19)
                self.dependeSiguiente("=", linea, 20)
                pass
            # ******* Dependencia *******
            elif linea[self.index] == "&":
                self.siguienteEstado(linea, 21)
                self.dependeSiguiente("&", linea, 22)
                pass
            elif linea[self.index] == "|":
                self.siguienteEstado(linea, 23)
                self.dependeSiguiente("|", linea, 24)
                pass
            elif linea[self.index] == "$":
                self.siguienteEstado(linea, 25)
                pass
            else:
                # Error
                self.siguienteEstado(linea, 26)
                pass
            pass
        except IndexError:
            pass
        pass

    def tipoReservado(self):
        if self.simbolo == "int" or self.simbolo == "float" or self.simbolo == "void":
            self.tipo = 4
            pass
        elif self.simbolo == "if":
            self.tipo = 19
            pass
        elif self.simbolo == "while":
            self.tipo = 20
            pass
        elif self.simbolo == "return":
            self.tipo = 21
            pass
        elif self.simbolo == "else":
            self.tipo = 22
            pass
        pass

    def dividir(self):
        if self.simbolo == "(":
            self.tipo = 14
            pass
        elif self.simbolo == ")":
            self.tipo = 15
            pass
        elif self.simbolo == "{":
            self.tipo = 16
            pass
        elif self.simbolo == "}":
            self.tipo = 17
            pass
        """
        elif self.simbolo == "[":
            self.tipo = 16
            pass
        elif self.simbolo == "]":
            self.tipo = 17
            pass
        """
        pass

    def imprimir(self):
        print(self.simbolo + "\t\t", end="")
        print(self.tipo)
        pass

    def tokens(self, linea):
        self.index = 0
        self.estado = 0
        self.simbolo = ""

        linea = self.espacios(linea)

        self.index = 0

        if self.index < len(linea):
            self.analizar(linea)

            # funciones dependientes
            if self.estado == 2 or self.estado == 13 or self.estado == 14 or self.estado == 15:
                self.estados_aceptados[self.estado]()
                pass
            else:
                # directos
                self.tipo = self.estados_aceptados.get(self.estado, -1)
                if self.tipo == -1:
                    self.error = True
                    pass
                pass
            pass

            # self.imprimir()
            if self.index < len(linea):
                linea = linea[self.index:]
                pass
            else:
                linea = ""
                pass
            return linea
        pass
