# -*- ENCODING: UTF-8 -*-
"""
 * File:   Sintactico.py
 * Author: Miguel Ochoa Hernandez
 *

"""

from __future__ import print_function
import os
from Arbol.Nodo import *
from Arbol.Terminales import *
from Componentes.Leer import Leer
from Componentes.Lexico import Lexico
from Componentes.Pila import *
from Componentes.Excepciones import *

__author__ = "Miguel Ochoa Hernandez"


class Sintactico(object):

    """Analizador Sintactico para el lenguaje"""

    def __init__(self):
        super(Sintactico, self).__init__()
        self.error = False
        self.pila = []
        self.reglas = dict()

        numero_columnas = 4
        numero_filas = 5

        base = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))

        base = os.path.join(base, "Gramatica")

        with open(os.path.join(base, "compilador.lr"), "r") as archivo:
            cantidad = int(archivo.readline())

            for x in range(0, cantidad):
                linea = archivo.readline().replace("\r", "").replace(
                    "\n", "").replace("\t", " ").split(" ")

                id_Nt = int(linea[0])
                reduccion = int(linea[1])
                nt = linea[2]

                self.reglas[x] = (NoTerminal(nt, reduccion, id_Nt))
                pass

            # print(len(self.reglas))

            linea = archivo.readline().replace("\r", "").replace(
                "\n", "").replace("\t", " ").split(" ")

            numero_filas = int(linea[0])
            numero_columnas = int(linea[1])

            self.matriz = [[0 for x in range(numero_columnas)]
                           for x in range(numero_filas)]

            for i in range(0, numero_filas):
                linea = archivo.readline().replace("\r", "").replace(
                    "\n", "").replace("\t", " ").split(" ")
                for j in range(0, numero_columnas):
                    self.matriz[i][j] = int(linea[j])
                    pass
                pass
            pass

        nodo = Terminal("$")
        self.pila.append(nodo)
        nodo = Estado(0)
        self.pila.append(nodo)

        pass

    def reducciones(self, regla):
        nodo = None
        extraer = self.reglas.get(regla)

        if regla == 0:
            nodo = Programa()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 1:
            nodo = Definiciones()
            # print("################### Aqui ya es nulo 1 ####################")
            pass
        elif regla == 2:
            nodo = Definiciones()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 3:
            nodo = Definicion()
            self.pila = nodo.definicionVariable(self.pila)
            pass
        elif regla == 4:
            nodo = Definicion()
            self.pila = nodo.definicioFuncion(self.pila)
            pass
        elif regla == 5:
            nodo = DefinicionVariable()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 6:
            nodo = ListaVariables()
            # print("################### Aqui ya es nulo 6 ####################")
            pass
        elif regla == 7:
            nodo = ListaVariables()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 8:
            nodo = DefinicionFuncion()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 9:
            nodo = Parametros()
            # print("################### Aqui ya es nulo 9 ####################")
            pass
        elif regla == 10:
            nodo = Parametros()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 11:
            nodo = ListaParametros()
            # print("################### Aqui ya es nulo 11 ####################")
            pass
        elif regla == 12:
            nodo = ListaParametros()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 13:
            nodo = BloqueFuncion()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 14:
            nodo = DefinicionesLocales()
            # print("################### Aqui ya es nulo 14 ####################")
            pass
        elif regla == 15:
            nodo = DefinicionesLocales()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 16:
            nodo = DefinicionLocal()
            self.pila = nodo.definicionVariable(self.pila)
            pass
        elif regla == 17:
            nodo = DefinicionLocal()
            self.pila = nodo.definicionSentencia(self.pila)
            pass
        # Sentencias
        ######################################################
        elif regla == 18:
            nodo = Sentencias()
            # print("################### Aqui ya es nulo 18 ####################")
            pass
        elif regla == 19:
            nodo = Sentencias()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 20:
            nodo = Asignacion()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 21:
            nodo = CondicionalSimple()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 22:
            nodo = Mientras()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 23:
            nodo = Retorno()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 24:
            nodo = Sentencia()
            self.pila = nodo.inicializar(self.pila)
            pass
        #
        ######################################################
        elif regla == 25:
            nodo = CondicionalCompuesta()
            # print("################### Aqui ya es nulo 25 ####################")
            pass
        elif regla == 26:
            nodo = CondicionalCompuesta()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 27:
            nodo = Bloque()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 28:
            nodo = ValorRegresa()
            # print("################### Aqui ya es nulo 28 ####################")
            pass
        elif regla == 29:
            nodo = ValorRegresa()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 30:
            nodo = Argumentos()
            # print("################### Aqui ya es nulo 30 ####################")
            pass
        elif regla == 31:
            nodo = Argumentos()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 32:
            nodo = ListaArgumentos()
            # print("################### Aqui ya es nulo 32 ####################")
            pass
        elif regla == 33:
            nodo = ListaArgumentos()
            self.pila = nodo.inicializar(self.pila)
            pass
        # Terminos
        ######################################################
        elif regla == 34:
            nodo = Termino()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 35:
            nodo = Identificador()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 36:
            nodo = Entero()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 37:
            nodo = Real()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 38:
            nodo = Cadena()
            self.pila = nodo.inicializar(self.pila)
            pass
        #
        ######################################################
        elif regla == 39:
            nodo = LlamadaFuncion()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 40:
            nodo = SentenciaBloque()
            self.pila = nodo.definicionSentencia(self.pila)
            pass
        elif regla == 41:
            nodo = SentenciaBloque()
            self.pila = nodo.definicionBloque(self.pila)
            pass
        # Expresiones
        ######################################################
        elif regla == 42:
            nodo = Expresion()
            self.pila = nodo.multiExpresion(self.pila)
            pass
        elif regla == 43:
            nodo = OperadorSuma()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 44:
            nodo = OperadorNot()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 45:
            nodo = OperadorMultiplicacion()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 46:
            nodo = OperadorSuma()
            self.pila = nodo.inicializar(self.pila, 2)
            pass
        elif regla == 47:
            nodo = OperadorRelacional()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 48:
            nodo = OperadorIgualdad()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 49:
            nodo = OperadorAnd()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 50:
            nodo = OperadorOr()
            self.pila = nodo.inicializar(self.pila)
            pass
        elif regla == 51:
            nodo = Termino()
            self.pila = nodo.inicializar(self.pila)
            pass
        else:
            # print("################### Aqui ya es nulo for ####################")
            for x in range(0, extraer.reduccion * 2):
                self.pila.pop()
                pass
            pass

        return nodo
        pass

    def imprimirPila(self):
        copia_pila = self.pila
        tabulaciones = "\t"
        print("Pila:    ", end="")
        if len(copia_pila) < 7:
            tabulaciones += "\t"
            pass

        for i in copia_pila:
            i.imprimir()
            pass
        # print(tabulaciones + "|\t", end="")
        pass

    def apilar(self, encabezado):
        self.pila.append(encabezado)
        pass

    def desapilar(self):
        return self.pila.pop()
        pass

    def encabezadoDePila(self):
        return self.pila[len(self.pila) - 1]
        pass

    def imprimir(self, elemento="", resto_linea="", reduccion="apilar", primero=False):
        if not primero:
            print("| Accion:    {0} -> {1}".format(elemento, reduccion))
            print()
            pass
        self.imprimirPila()
        print()
        print("Entrada {0}\t\t".format(resto_linea), end="")
        pass

    def entrada(self):
        arbol = None
        nodo = None
        lectura = Leer()
        nombre = lectura.pedirArchivo()
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
                pass

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
                        pass
                    elif accion > 0:

                        terminal = Terminal(lexico.simbolo)
                        self.pila.append(terminal)
                        estado = Estado(accion)
                        self.pila.append(estado)

                        self.imprimir(elemento=terminal.terminal,
                                      resto_linea=resto_linea)
                        copia_resto = resto_linea
                        resto_linea = lexico.tokens(resto_linea)

                        pass
                    elif accion < 0:

                        regla = (accion * -1) - 2

                        nodo = self.reducciones(regla)

                        extraer = self.reglas.get(regla)

                        nodo_no_terminal = NoTerminal(
                            extraer.no_terminal, extraer.reduccion, extraer.estado)

                        nodo_no_terminal.nodo = nodo

                        # for x in range(0, extraer.reduccion * 2):
                        #    self.pila.pop()
                        #    pass

                        accion = self.matriz[self.encabezadoDePila().estado][
                            extraer.estado]

                        self.pila.append(nodo_no_terminal)
                        # self.pila.append(extraer)

                        estado = Estado(accion)
                        self.pila.append(estado)

                        self.imprimir(elemento=extraer.no_terminal,
                                      reduccion=extraer.reduccion, resto_linea=copia_resto)

                        pass
                    else:
                        print("| Accion:    Error Sintactico")
                        self.error = True
                        break
                        pass
                    pass
                else:
                    print("| Accion:    Error Lexico")
                    break
                    pass
                pass

            # if lexico.error or self.error:
            #     break
            #     pass

        if terminar == 1:
            print("| Accion:    Aceptada")
            self.pila.pop()
            arbol = self.pila.pop().nodo
            print()
            arbol.imprimir("")
            pass
        else:
            arbol = None
            pass

        return arbol
        pass
