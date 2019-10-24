#!/usr/bin/env python

# -*- ENCODING: UTF-8 -*-
"""
 * File:   Sintactico.py
 * Author: Miguel Ochoa Hernandez
 *

"""

from __future__ import print_function

import os

from Arbol.Nodo import Expresion

from Arbol.Terminales import Programa
from Arbol.Terminales import Termino
# from Arbol.Terminales import Tipo
from Arbol.Terminales import Identificador
from Arbol.Terminales import Entero
from Arbol.Terminales import Real
from Arbol.Terminales import Cadena
from Arbol.Terminales import LlamadaFuncion
from Arbol.Terminales import OperadorSuma
from Arbol.Terminales import OperadorNot
from Arbol.Terminales import OperadorMultiplicacion
from Arbol.Terminales import OperadorRelacional
from Arbol.Terminales import OperadorIgualdad
from Arbol.Terminales import OperadorAnd
from Arbol.Terminales import OperadorOr
from Arbol.Terminales import Bloque
from Arbol.Terminales import ValorRegresa
from Arbol.Terminales import Sentencia
from Arbol.Terminales import Asignacion
from Arbol.Terminales import ListaParametros
from Arbol.Terminales import ListaArgumentos
from Arbol.Terminales import ListaVariables
from Arbol.Terminales import Definicion
from Arbol.Terminales import DefinicionLocal
from Arbol.Terminales import SentenciaBloque
from Arbol.Terminales import Definiciones
from Arbol.Terminales import Sentencias
from Arbol.Terminales import DefinicionesLocales
from Arbol.Terminales import BloqueFuncion
from Arbol.Terminales import Parametros
from Arbol.Terminales import DefinicionFuncion
from Arbol.Terminales import DefinicionVariable
from Arbol.Terminales import Argumentos
from Arbol.Terminales import CondicionalSimple
from Arbol.Terminales import Mientras
from Arbol.Terminales import Retorno
from Arbol.Terminales import CondicionalCompuesta

from .Lexico import Lexico
from .Pila import Terminal, NoTerminal, Estado
# from .Excepciones import Errores

__author__ = "Miguel Ochoa Hernandez"


class Sintactico():
    """Analizador Sintactico para el lenguaje"""

    def __init__(self):
        super(Sintactico, self).__init__()
        self.error = False
        self.pila = []
        self.reglas = dict()

        numero_columnas = 4
        numero_filas = 5

        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        base = os.path.join(base, "Gramatica")

        with open(os.path.join(base, "compilador.lr"), "r") as archivo:
            cantidad = int(archivo.readline())

            for tipo_de_regla in range(0, cantidad):
                linea = archivo.readline().replace("\r", "").replace(
                    "\n", "").replace("\t", " ").split(" ")

                id_Nt = int(linea[0])
                reduccion = int(linea[1])
                nt = linea[2]

                self.reglas[tipo_de_regla] = (NoTerminal(nt, reduccion, id_Nt))

            # print(len(self.reglas))

            linea = archivo.readline().replace("\r",
                                               "").replace("\n", "").replace(
                                                   "\t", " ").split(" ")

            numero_filas = int(linea[0])
            numero_columnas = int(linea[1])

            self.matriz = [[0 for x in range(numero_columnas)]
                           for x in range(numero_filas)]

            for i in range(0, numero_filas):
                linea = archivo.readline().replace("\r", "").replace(
                    "\n", "").replace("\t", " ").split(" ")
                for j in range(0, numero_columnas):
                    self.matriz[i][j] = int(linea[j])

        nodo = Terminal("$")
        self.pila.append(nodo)
        nodo = Estado(0)
        self.pila.append(nodo)

    def reducciones(self, regla):
        nodo = None
        extraer = self.reglas.get(regla)

        if regla == 0:
            nodo = Programa()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 1:
            nodo = Definiciones()
            # print("################### Aqui ya es nulo 1 ####################")
        elif regla == 2:
            nodo = Definiciones()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 3:
            nodo = Definicion()
            self.pila = nodo.definicionVariable(self.pila)
        elif regla == 4:
            nodo = Definicion()
            self.pila = nodo.definicioFuncion(self.pila)
        elif regla == 5:
            nodo = DefinicionVariable()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 6:
            nodo = ListaVariables()
            # print("################### Aqui ya es nulo 6 ####################")
        elif regla == 7:
            nodo = ListaVariables()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 8:
            nodo = DefinicionFuncion()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 9:
            nodo = Parametros()
            # print("################### Aqui ya es nulo 9 ####################")
        elif regla == 10:
            nodo = Parametros()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 11:
            nodo = ListaParametros()
            # print("################### Aqui ya es nulo 11 ####################")
        elif regla == 12:
            nodo = ListaParametros()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 13:
            nodo = BloqueFuncion()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 14:
            nodo = DefinicionesLocales()
            # print("################### Aqui ya es nulo 14 ####################")
        elif regla == 15:
            nodo = DefinicionesLocales()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 16:
            nodo = DefinicionLocal()
            self.pila = nodo.definicionVariable(self.pila)
        elif regla == 17:
            nodo = DefinicionLocal()
            self.pila = nodo.definicionSentencia(self.pila)
        # Sentencias
        ######################################################
        elif regla == 18:
            nodo = Sentencias()
            # print("################### Aqui ya es nulo 18 ####################")
        elif regla == 19:
            nodo = Sentencias()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 20:
            nodo = Asignacion()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 21:
            nodo = CondicionalSimple()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 22:
            nodo = Mientras()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 23:
            nodo = Retorno()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 24:
            nodo = Sentencia()
            self.pila = nodo.inicializar(self.pila)
        #
        ######################################################
        elif regla == 25:
            nodo = CondicionalCompuesta()
            # print("################# Aqui ya es nulo 25 ##################")
        elif regla == 26:
            nodo = CondicionalCompuesta()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 27:
            nodo = Bloque()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 28:
            nodo = ValorRegresa()
            # print("################# Aqui ya es nulo 28 ##################")
        elif regla == 29:
            nodo = ValorRegresa()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 30:
            nodo = Argumentos()
            # print("################# Aqui ya es nulo 30 ###################")
        elif regla == 31:
            nodo = Argumentos()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 32:
            nodo = ListaArgumentos()
            # print("################# Aqui ya es nulo 32 ###################")
        elif regla == 33:
            nodo = ListaArgumentos()
            self.pila = nodo.inicializar(self.pila)
        # Terminos
        ######################################################
        elif regla == 34:
            nodo = Termino()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 35:
            nodo = Identificador()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 36:
            nodo = Entero()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 37:
            nodo = Real()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 38:
            nodo = Cadena()
            self.pila = nodo.inicializar(self.pila)
        #
        ######################################################
        elif regla == 39:
            nodo = LlamadaFuncion()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 40:
            nodo = SentenciaBloque()
            self.pila = nodo.definicionSentencia(self.pila)
        elif regla == 41:
            nodo = SentenciaBloque()
            self.pila = nodo.definicionBloque(self.pila)
        # Expresiones
        ######################################################
        elif regla == 42:
            nodo = Expresion()
            self.pila = nodo.multiExpresion(self.pila)
        elif regla == 43:
            nodo = OperadorSuma()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 44:
            nodo = OperadorNot()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 45:
            nodo = OperadorMultiplicacion()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 46:
            nodo = OperadorSuma()
            self.pila = nodo.inicializar(self.pila, 2)
        elif regla == 47:
            nodo = OperadorRelacional()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 48:
            nodo = OperadorIgualdad()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 49:
            nodo = OperadorAnd()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 50:
            nodo = OperadorOr()
            self.pila = nodo.inicializar(self.pila)
        elif regla == 51:
            nodo = Termino()
            self.pila = nodo.inicializar(self.pila)
        else:
            # print("################# Aqui ya es nulo for ##################")
            for _ in range(0, extraer.reduccion * 2):
                self.pila.pop()

        return nodo

    def imprimirPila(self):
        copia_pila = self.pila
        tabulaciones = "\t"
        print("Pila:    ", end="")
        if len(copia_pila) < 7:
            tabulaciones += "\t"

        for i in copia_pila:
            i.imprimir()
        # print(tabulaciones + "|\t", end="")

    def apilar(self, encabezado):
        self.pila.append(encabezado)

    def desapilar(self):
        return self.pila.pop()

    def encabezadoDePila(self):
        return self.pila[len(self.pila) - 1]

    def imprimir(self,
                 elemento="",
                 resto_linea="",
                 reduccion="apilar",
                 primero=False):
        if not primero:
            print("| Accion:    {0} -> {1}".format(elemento, reduccion))
            print()
        self.imprimirPila()
        print()
        print("Entrada {0}\t\t".format(resto_linea), end="")

    def entrada(self, filename: str):
        arbol = None
        nodo = None
        # lectura = Leer()
        nombre = filename
        lexico = Lexico()
        encabezado = 0
        accion = 0
        resto_linea = ""
        terminar = 0
        copia_resto = ""
        with open(nombre, "r") as archivo:

            linea = archivo.readlines()

            for x in linea:
                resto_linea += x

            resto_linea = resto_linea.replace("\n", "").replace("\r", "")
            resto_linea = resto_linea + "$"
            copia_resto = resto_linea
            # print(resto_linea + "\t|\t", end="")
            self.imprimir(resto_linea=copia_resto, primero=True)

            resto_linea = lexico.tokens(resto_linea)
            copia_resto = resto_linea

            while terminar == 0:

                if not lexico.error:
                    encabezado = self.encabezadoDePila()
                    accion = self.matriz[encabezado.estado][lexico.tipo]

                    if accion == -1:
                        terminar = 1
                        break
                    elif accion > 0:
                        terminal = Terminal(lexico.simbolo)
                        self.pila.append(terminal)
                        estado = Estado(accion)
                        self.pila.append(estado)

                        self.imprimir(elemento=terminal.terminal,
                                      resto_linea=resto_linea)
                        copia_resto = resto_linea
                        resto_linea = lexico.tokens(resto_linea)

                    elif accion < 0:
                        regla = (accion * -1) - 2
                        nodo = self.reducciones(regla)
                        extraer = self.reglas.get(regla)
                        nodo_no_terminal = NoTerminal(extraer.no_terminal,
                                                      extraer.reduccion,
                                                      extraer.estado)
                        nodo_no_terminal.nodo = nodo

                        # for x in range(0, extraer.reduccion * 2):
                        #    self.pila.pop()

                        accion = self.matriz[self.encabezadoDePila().estado][
                            extraer.estado]

                        self.pila.append(nodo_no_terminal)
                        # self.pila.append(extraer)

                        estado = Estado(accion)
                        self.pila.append(estado)

                        self.imprimir(elemento=extraer.no_terminal,
                                      reduccion=extraer.reduccion,
                                      resto_linea=copia_resto)
                    else:
                        print("| Accion:    Error Sintactico")
                        self.error = True
                        break
                else:
                    print("| Accion:    Error Lexico")
                    break

            # if lexico.error or self.error:
            #     break

        if terminar == 1:
            print("| Accion:    Aceptada")
            self.pila.pop()
            arbol = self.pila.pop().nodo
            print()
            arbol.imprimir("")
        else:
            arbol = None
        return arbol

