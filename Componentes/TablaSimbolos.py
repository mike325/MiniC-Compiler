# -*- ENCODING: UTF-8 -*-
"""
 * File:   TablaSimbolos.py
 * Author: Miguel Ochoa Hernandez
 * C0digo: 212355068
 * Taller de compiladores
 *
"""

from __future__ import print_function
from Componentes import Globales
from Componentes.Excepciones import *
from Arbol.Nodo import *
# import Componentes
# from Componentes import Globales

__author__ = "Miguel Ochoa Hernandez"


class ElementoTabla(object):

    """docstring for ElementoTabla"""

    def __init__(self):
        super(ElementoTabla, self).__init__()
        self.ambito = ""
        self.tipo = ""
        self.simbolo = ""
        pass

    def esVariable(self):
        return False
        pass

    def esVarLocal(self):
        return False
        pass

    def esFuncion(self):
        return False
        pass


class Variable(ElementoTabla):

    """docstring for Variable"""

    def __init__(self, tipo, simbolo, ambito):
        super(Variable, self).__init__()
        self.tipo = str(tipo)
        self.simbolo = str(simbolo)
        self.ambito = str(ambito)
        # print("Variable {0} en el ambito {1}".format(self.simbolo, self.ambito))
        self.local = (self.ambito != "")
        pass

    def esVariable(self):
        return True
        pass

    def esVarLocal(self):
        return self.local
        pass


class Funcion(ElementoTabla):

    """docstring for Funcion"""

    def __init__(self, tipo, simbolo, parametros, ambito):
        super(Funcion, self).__init__()
        self.ambito = str(ambito)
        self.tipo = str(tipo)
        self.simbolo = str(simbolo)
        self.parametros = parametros
        self.lista_parametros = []
        pass

    def esFuncion(self):
        return True
        pass

    def agregaParametro(self, simbolo, tipo_dato):
        # print("Variable {0} en ambito {1}".format(simbolo, Globales.ambito))
        identificador = simbolo
        tipo = tipo_dato
        elemento = Variable(tipo, identificador, Globales.ambito)
        self.lista_parametros.append(elemento)

        encontrado = Globales.tabla_simbolos.buscaIdentificador(simbolo)
        if encontrado == "":
            Globales.tabla_simbolos.agregaVariable(simbolo, tipo_dato)
            pass
        else:
            raise Errores("La variable {0} en la funcion {1} ya esta previamente definida".format(simbolo, Globales.ambito))
            pass
        pass


class TablaSimbolos(object):

    """Analizador TablaSimbolos"""

    def __init__(self, lista_errores=[]):
        self.tabla = [list() for x in range(0, 211)]
        self.variable_local = None
        self.variable_globa = None
        self.funcion = None
        # self.lista_errores = lista_errores
        pass

    def hash(self, ambito_variable):
        posicion = 0
        base = 3
        i = len(ambito_variable)
        while i > 0:
            posicion += (ord(ambito_variable[i - 1]) * base**(i - 1)
                         * i + (ord(ambito_variable[i - 1]) * i))
            i -=1
            pass
        posicion %= 211

        return posicion
        pass

    def agregaElemento(self, elemento):
        posicion = self.hash(elemento.ambito)
        self.tabla[posicion].append(elemento)
        pass

    def muestra(self):
        pass

    def varGlobalDefinida(self, variable):
        pass

    def funcionDefinida(self, funcion):
        pass

    def varLocalDefinida(self, variable, funcion):
        pass

    def actualizarFuncion(self, simbolo, tipo_dato):
        funcion, posicion_funcion = Globales.tabla_simbolos.buscaFuncion(Globales.ambito)
        # print("Posicion de la funcion {0}: {1}, ambito {2}".format(funcion.simbolo, posicion_funcion, Globales.ambito))
        funcion.agregaParametro(simbolo, tipo_dato)

        posicion = self.hash("global")
        # print("Prueba nombre {0}".format(self.tabla[posicion][posicion_funcion].simbolo))
        self.tabla[posicion][posicion_funcion] = funcion
        pass

    def buscaFuncion(self, simbolo):
        encontrado = False
        tipo = ""
        revisar_ambitos = []
        funcion = None
        pos = 0
        revisar_ambitos.append("global")

        while len(revisar_ambitos) > 0 and not encontrado:
            ambito_actual = revisar_ambitos.pop()
            posicion = self.hash(ambito_actual)
            variables_en_ambito = self.tabla[posicion]

            for j in range(0, len(variables_en_ambito)):
                if variables_en_ambito[j].simbolo == simbolo:
                    funcion = variables_en_ambito[j]
                    pos = j
                    encontrado = True
                    break
                    pass
                pass
            pass
        return funcion, pos
        pass


    def buscaIdentificador(self, simbolo):
        encontrado = False
        tipo = ""
        revisar_ambitos = []

        for i in range(0, len(Globales.ambitos_anteriores)):
            revisar_ambitos.append(Globales.ambitos_anteriores[i])
            pass
        revisar_ambitos.append(Globales.ambito)

        while len(revisar_ambitos) > 0 and not encontrado:
            ambito_actual = revisar_ambitos.pop()
            posicion = self.hash(ambito_actual)
            variables_en_ambito = self.tabla[posicion]
            # print("ambito {0}".format(ambito_actual))
            for j in variables_en_ambito:
                # print("Identificador actual {0}".format(j.simbolo))
                # print("Identificador buscado {0}".format(simbolo))
                if j.simbolo == simbolo:
                    tipo = j.tipo
                    encontrado = True
                    break
                    pass
                pass
            pass
        return tipo
        pass

    def agregaVariable(self, simbolo, tipo_dato):
        # print("Nueva variable {0} en el ambito {1}".format(simbolo, Globales.ambito))
        identificador = simbolo
        tipo = tipo_dato
        elemento = Variable(tipo, identificador, Globales.ambito)
        self.agregaElemento(elemento)
        pass

    def agregaFuncion(self, defFunc):
        # print("Nueva funcion {0} en el ambito {1}".format(defFunc.identificador.simbolo, Globales.ambito))
        tipo = defFunc.tipo_dato
        identificador = defFunc.identificador.simbolo
        elemento = Funcion(tipo, identificador, defFunc.parametros, Globales.ambito)
        self.agregaElemento(elemento)
        pass