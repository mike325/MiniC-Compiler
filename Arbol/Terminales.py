# -*- ENCODING: UTF-8 -*-
"""
 * File:   Expresion.py
 * Author: Miguel Ochoa Hernandez
 *
"""

from Arbol.Nodo import Nodo, Expresion
from Componentes import Globales
from Componentes.Excepciones import Errores

__author__ = "Miguel Ochoa Hernandez"

inversiones = {
    "<": "JGE",
    ">": "JLE",
    "<=": "JG",
    ">=": "JL",
    "==": "JNE",
    "~=": "JE",
}

sumas = {"+": "ADD", "-": "SUBB"}
multimplicaciones = {"*": "MUL", "/": "DIV"}

tipos_ensamblador = {"i": "dword", "f": "real4"}


class Programa(Nodo):
    """docstring for Programa"""
    def __init__(self):
        super(Programa, self).__init__()
        self.definiciones = None

    def inicializar(self, pila):
        pila.pop()
        self.definiciones = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Programa>".format(tabulaciones))
        self.definiciones.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        self.definiciones.decideTipo()
        if self.definiciones.tipo_dato != "e":
            self.tipo_dato = "v"

    # pendiente
    def generacionCodigo(self):
        # print("Programa.generacionCodigo")
        # return self.sentencias.generacionCodigo()
        global tipos_ensamblador
        codigo = ""
        codigo += ".386\n.model flat, stdcall\noption casemap:none ;labels are case-sensitive now\n"
        codigo += "include \\masm32\\macros\\macros.asm\ninclude \\masm32\\include\\masm32.inc\n"
        codigo += "include \\masm32\\include\\kernel32.inc\nincludelib \\masm32\\lib\\masm32.lib\n"
        codigo += "includelib \\masm32\\lib\\kernel32.lib\n.data\n.data?\n"
        #
        # variables globales
        #
        posicion = Globales.tabla_simbolos.hash("global")

        for variable in Globales.tabla_simbolos.tabla[posicion]:
            if variable.esVariable():
                codigo += "\t{0}\t{1}\t?\n".format(
                    variable.simbolo, tipos_ensamblador.get(variable.tipo))
        codigo += ".code\ninicio:\n\ncall main\nexit\n\n"
        codigo += "{0}".format(self.definiciones.generacionCodigo())
        codigo += "\nend\tinicio"
        return codigo


# primitivos
#################################################################


class Termino(Expresion):
    """docstring for Termino"""
    def __init__(self):
        super(Termino, self).__init__()
        self.llamada_funcion = None

    def inicializar(self, pila):
        pila.pop()
        self.llamada_funcion = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Termino>".format(tabulaciones))
        self.llamada_funcion.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        self.llamada_funcion.decideTipo()
        if self.llamada_funcion.tipo_dato != "e":
            self.tipo_dato = self.llamada_funcion.tipo_dato
        else:
            raise Errores(
                "El termino no tiene un tipo de dato correcto en el ambito {0}"
                .format(Globales.ambito))

    def generacionCodigo(self):
        codigo = ""
        codigo += self.llamada_funcion.generacionCodigo()
        return codigo


class Tipo(Nodo):
    """docstring for Tipo"""
    def __init__(self, terminal):
        super(Tipo, self).__init__()
        self.simbolo = terminal

    def inicializar(self, terminal):
        self.simbolo = terminal

    def imprimir(self, tabulaciones):
        print("{0}<Tipo>".format(tabulaciones))
        print("{0}{1}".format(tabulaciones, self.simbolo))

    def decideTipo(self):
        tipos_validos = {"int": "i", "float": "f", "string": "s", "void": "v"}
        self.tipo_dato = tipos_validos.get(self.simbolo, "e")
        if self.tipo_dato == "e":
            raise Errores(
                "El tipo de dato primitivo {0} en el ambito {1} no es aceptado"
                .format(self.simbolo, Globales.ambito))

    def generacionCodigo(self):
        pass


class Identificador(Termino):
    """docstring for Identificador"""
    def __init__(self):
        super(Identificador, self).__init__()
        self.simbolo = ""

    def inicializar(self, pila):
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        if not (self.simbolo is None) and self.simbolo != "":
            print("{0}<Identificador>".format(tabulaciones))
            print("{0}{1}".format(tabulaciones, self.simbolo))

    def decideTipo(self):
        if self.simbolo == "":
            self.tipo_dato = "v"
        else:
            self.tipo_dato = "e"
            # print("Identificador {0}".format(self.simbolo))
            tipo = Globales.tabla_simbolos.buscaIdentificador(self.simbolo)

            if len(tipo) > 0:
                # print("Identificador {0} con tipo {1} encontrado en el ambito {2}".format(self.simbolo, tipo, Globales.ambito))
                self.tipo_dato = tipo
            else:
                # print("Identificador {0} No encontrado".format(self.simbolo))
                # raise Errores("El identificador {0} no declarada previamente en el ambito {1}".format(
                # self.simbolo, Globales.ambito))
                pass

    def generacionCodigo(self):
        codigo = ""
        codigo += "PUSH {0}\n".format(self.simbolo)
        return codigo


class Entero(Termino):
    """docstring for Entero"""
    def __init__(self):
        super(Entero, self).__init__()

    def inicializar(self, pila):
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Entero>".format(tabulaciones))
        print("{0}{1}".format(tabulaciones, self.simbolo))

    def decideTipo(self):
        self.tipo_dato = "i"

    def generacionCodigo(self):
        codigo = ""
        codigo += "PUSH {0}\n".format(self.simbolo)
        return codigo


class Real(Termino):
    """docstring for Real"""
    def __init__(self):
        super(Real, self).__init__()

    def inicializar(self, pila):
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Real>".format(tabulaciones))
        print("{0}{1}".format(tabulaciones, self.simbolo))

    def decideTipo(self):
        self.tipo_dato = "f"

    def generacionCodigo(self):
        codigo = ""
        codigo += "PUSH {0}\n".format(self.simbolo)
        return codigo


class Cadena(Termino):
    """docstring for Cadena"""
    def __init__(self):
        super(Cadena, self).__init__()

    def inicializar(self, pila):
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Cadena>".format(tabulaciones))
        print("{0}{1}".format(tabulaciones, self.simbolo))

    def decideTipo(self):
        self.tipo_dato = "s"

    def generacionCodigo(self):
        codigo = ""
        codigo += "PUSH {0}\n".format(self.simbolo)
        return codigo


class LlamadaFuncion(Termino):
    """docstring for LlamadaFuncion"""
    def __init__(self):
        super(LlamadaFuncion, self).__init__()
        self.argumentos = None
        self.identificador = Identificador()

    def inicializar(self, pila):
        pila.pop()
        pila.pop()
        pila.pop()

        self.argumentos = pila.pop().nodo

        pila.pop()
        pila.pop()
        pila.pop()

        self.identificador.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<LlamadaFuncion>".format(tabulaciones))
        self.identificador.imprimir(tabulaciones + "\t")
        self.argumentos.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        self.identificador.decideTipo()

        if self.identificador.tipo_dato != "e":
            if not (self.argumentos is None):

                self.argumentos.decideRecursivo(self.identificador.simbolo)
                if self.argumentos.tipo_dato != "e":
                    self.tipo_dato = "v"
                else:
                    raise Errores(
                        "Los argumentos de la funcion {0}, no coinciden".
                        format(self.identificador.simbolo))
            else:
                funcion, pos = Globales.tabla_simbolos.buscaFuncion(
                    self.identificador.simbolo)
                if len(funcion.lista_parametros) == 0:
                    self.tipo_dato = "v"
                else:
                    raise Errores(
                        "Los argumentos de la funcion {0}, no coinciden".
                        format(self.identificador.simbolo))
        else:
            raise Errores(
                "El identificador de funcion {0} no esta declarado".format(
                    self.identificador.simbolo))

    # Pendiente
    def generacionCodigo(self):
        codigo = "\n"
        if not (self.argumentos is None):
            codigo += self.argumentos.generacionCodigo()
        codigo += "call {0}\n".format(self.identificador.simbolo)
        return codigo


# Fin primitivos
#################################################################

# Expresiones
#################################################################


class OperadorSuma(Expresion):
    """docstring for OperadorSuma"""
    def __init__(self):
        super(OperadorSuma, self).__init__()
        self.expresion = None

    def inicializar(self, pila, tipo=1):
        pila.pop()

        if tipo == 1:
            self.expresion = pila.pop().nodo
            pila.pop()
            self.simbolo = pila.pop().terminal
        else:
            self.derecha = pila.pop().nodo
            pila.pop()
            self.simbolo = pila.pop().terminal
            pila.pop()
            self.izquierdo = pila.pop().nodo

        return pila

    def imprimir(self, tabulaciones):
        print("{0}<OperadorSuma>".format(tabulaciones))
        if not (self.expresion is None):
            print("{0}{1}".format(tabulaciones, self.simbolo))
            self.expresion.imprimir(tabulaciones + "\t")
        else:
            self.izquierdo.imprimir(tabulaciones + "\t")
            print("{0}{1}".format(tabulaciones, self.simbolo))
            self.derecha.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.expresion is None):
            self.expresion.decideTipo()
            if self.expresion.tipo_dato != "e":
                self.tipo_dato = self.expresion.tipo_dato
            else:
                raise Errores(
                    "Los tipos de datos no coinciden en la operacion de suma en el ambito {0}"
                    .format(Globales.ambito))
        else:
            self.izquierdo.decideTipo()
            self.derecha.decideTipo()
            if self.izquierdo.tipo_dato == "i" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
                self.tipo_dato = "i"
            elif self.izquierdo.tipo_dato == "f" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
                self.tipo_dato = "f"
            elif self.izquierdo.tipo_dato == "s" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
                self.tipo_dato = "s"
            elif self.izquierdo.tipo_dato == "v" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
                self.tipo_dato = "v"
            else:
                raise Errores(
                    "Los tipos de datos no coinciden en la operacion de suma en el ambito {0}"
                    .format(Globales.ambito))

    def generacionCodigo(self):
        global sumas
        codigo = "\n"
        izquierdo = ""
        derecho = ""

        izquierdo += self.izquierdo.generacionCodigo()
        derecho += self.derecha.generacionCodigo()
        codigo += "{0}".format(izquierdo)
        codigo += "{0}".format(derecho)

        codigo += "POP eax\n"
        codigo += "POP ecx\n"
        codigo += "{0} eax,ecx\n".format(sumas.get(self.simbolo))
        codigo += "PUSH eax\n"
        return codigo


class OperadorNot(Expresion):
    """docstring for OperadorNot"""
    def __init__(self):
        super(OperadorNot, self).__init__()
        self.expresion = None

    def inicializar(self, pila):
        pila.pop()
        self.expresion = pila.pop().nodo
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<OperadorNot>".format(tabulaciones))
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.expresion.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        if not (self.expresion is None):
            self.expresion.decideTipo()
            if self.expresion.tipo_dato != "e":
                self.tipo_dato = self.expresion.tipo_dato
            else:
                raise Errores(
                    "Los tipos de datos no coinciden en la negacion en el ambito {0}"
                    .format(Globales.ambito))
        else:
            raise Errores(
                "Los tipos de datos no coinciden en la negacion en el ambito {0}"
                .format(Globales.ambito))

    def generacionCodigo(self):
        global multimplicaciones
        codigo = "\n"
        expresion = ""

        expresion += self.expresion.generacionCodigo()
        codigo += "{0}".format(expresion)

        codigo += "POP eax\n"
        if self.tipo_dato == "i":
            codigo += "MUL -1\n"
        else:
            codigo += "MUL -1.0\n"
        codigo += "PUSH eax\n"
        return codigo


class OperadorMultiplicacion(Expresion):
    """docstring for OperadorMultiplicacion"""
    def __init__(self):
        super(OperadorMultiplicacion, self).__init__()

    def inicializar(self, pila):
        pila.pop()
        self.derecha = pila.pop().nodo
        pila.pop()
        self.simbolo = pila.pop().terminal
        pila.pop()
        self.izquierdo = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<OperadorMultiplicacion>".format(tabulaciones))
        self.izquierdo.imprimir(tabulaciones + "\t")
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.derecha.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        self.izquierdo.decideTipo()
        self.derecha.decideTipo()

        if self.izquierdo.tipo_dato == "i" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "i"
        elif self.izquierdo.tipo_dato == "f" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "f"
        elif self.izquierdo.tipo_dato == "s" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "s"
        elif self.izquierdo.tipo_dato == "v" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "v"
        else:
            raise Errores(
                "Los tipos de datos no coinciden en la multiplicacion en el ambito {0}"
                .format(Globales.ambito))

    def generacionCodigo(self):
        global multimplicaciones
        codigo = "\n"
        izquierdo = ""
        derecho = ""

        izquierdo += self.izquierdo.generacionCodigo()
        derecho += self.derecha.generacionCodigo()
        codigo += "{0}".format(izquierdo)
        codigo += "{0}".format(derecho)
        # codigo += "{0}".format(derecho)

        codigo += "POP ebx\n"
        codigo += "POP ecx\n"
        # codigo += "MOV eax,ecx\n"
        codigo += "{0} ecx\n".format(multimplicaciones.get(self.simbolo))
        codigo += "PUSH eax\n"
        return codigo


class OperadorRelacional(Expresion):
    """docstring for OperadorRelacional"""
    def __init__(self):
        super(OperadorRelacional, self).__init__()

    def inicializar(self, pila):
        pila.pop()
        self.derecha = pila.pop().nodo
        pila.pop()
        self.simbolo = pila.pop().terminal
        pila.pop()
        self.izquierdo = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<OperadorRelacional>".format(tabulaciones))
        self.izquierdo.imprimir(tabulaciones + "\t")
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.derecha.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        self.izquierdo.decideTipo()
        self.derecha.decideTipo()
        if self.izquierdo.tipo_dato == "i" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "i"
        elif self.izquierdo.tipo_dato == "f" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "f"
        elif self.izquierdo.tipo_dato == "s" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "s"
        elif self.izquierdo.tipo_dato == "v" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "v"
        else:
            raise Errores(
                "Los tipos de datos no coinciden en la comparacion en el ambito {0}"
                .format(Globales.ambito))

    # Pendiente
    def generacionCodigo(self):
        codigo = "\n"
        izquierdo = self.izquierdo.generacionCodigo()
        derecho = self.derecha.generacionCodigo()
        codigo += izquierdo
        codigo += derecho
        codigo += "POP ebx\n"
        codigo += "POP ecx\n"
        codigo += "SUBB ebx,ecx\n"
        codigo += "PUSH ebx\n"
        return codigo


class OperadorIgualdad(Expresion):
    """docstring for OperadorIgualdad"""
    def __init__(self):
        super(OperadorIgualdad, self).__init__()

    def inicializar(self, pila):
        pila.pop()
        self.derecha = pila.pop().nodo
        pila.pop()
        self.simbolo = pila.pop().terminal
        pila.pop()
        self.izquierdo = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<OperadorIgualdad>".format(tabulaciones))
        self.izquierdo.imprimir(tabulaciones + "\t")
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.derecha.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        self.izquierdo.decideTipo()
        self.derecha.decideTipo()
        if self.izquierdo.tipo_dato == "i" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "i"
        elif self.izquierdo.tipo_dato == "f" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "f"
        elif self.izquierdo.tipo_dato == "s" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "s"
        elif self.izquierdo.tipo_dato == "v" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "v"
        else:
            raise Errores(
                "Los tipos de datos no coinciden en la comparacion igualdad en el ambito {0}"
                .format(Globales.ambito))

    # Pendiente
    def generacionCodigo(self):
        codigo = "\n"
        izquierdo = self.izquierdo.generacionCodigo()
        derecho = self.derecha.generacionCodigo()
        codigo += izquierdo
        codigo += derecho
        codigo += "POP ebx\n"
        codigo += "POP ecx\n"
        codigo += "SUBB ebx,ecx\n"
        codigo += "PUSH ebx\n"
        return codigo


class OperadorAnd(Expresion):
    """docstring for OperadorAnd"""
    def __init__(self):
        super(OperadorAnd, self).__init__()

    def inicializar(self, pila):
        pila.pop()
        self.derecha = pila.pop().nodo
        pila.pop()
        self.simbolo = pila.pop().terminal
        pila.pop()
        self.izquierdo = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<OperadorAnd>".format(tabulaciones))
        self.izquierdo.imprimir(tabulaciones + "\t")
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.derecha.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        self.izquierdo.decideTipo()
        self.derecha.decideTipo()
        if self.izquierdo.tipo_dato == "i" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "i"
        elif self.izquierdo.tipo_dato == "f" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "f"
        elif self.izquierdo.tipo_dato == "s" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "s"
        elif self.izquierdo.tipo_dato == "v" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "v"
        else:
            raise Errores(
                "Los tipos de datos no coinciden en la comparacion AND en el ambito {0}"
                .format(Globales.ambito))

    # Pendiente
    def generacionCodigo(self):
        codigo = "\n"
        izquierdo = self.izquierdo.generacionCodigo()
        derecho = self.derecha.generacionCodigo()
        codigo += izquierdo
        codigo += derecho
        codigo += "POP ebx\n"
        codigo += "POP ecx\n"

        codigo += "SUBB ebx,ecx\n"
        codigo += "SUBB ebx,ecx\n"
        codigo += "PUSH 1\n"
        codigo += "PUSH -1\n"
        return codigo


class OperadorOr(Expresion):
    """docstring for OperadorOr"""
    def __init__(self):
        super(OperadorOr, self).__init__()

    def inicializar(self, pila):
        pila.pop()
        self.derecha = pila.pop().nodo
        pila.pop()
        self.simbolo = pila.pop().terminal
        pila.pop()
        self.izquierdo = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<OperadorOr>".format(tabulaciones))
        self.izquierdo.imprimir(tabulaciones + "\t")
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.derecha.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        self.izquierdo.decideTipo()
        self.derecha.decideTipo()

        if self.izquierdo.tipo_dato == "i" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "i"
        elif self.izquierdo.tipo_dato == "f" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "f"
        elif self.izquierdo.tipo_dato == "s" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "s"
        elif self.izquierdo.tipo_dato == "v" and self.izquierdo.tipo_dato == self.derecha.tipo_dato:
            self.tipo_dato = "v"
        else:
            raise Errores(
                "Los tipos de datos no coinciden en la comparacion OR en el ambito {0}"
                .format(Globales.ambito))

    # Pendiente
    def generacionCodigo(self):
        codigo = "\n"
        izquierdo = self.izquierdo.generacionCodigo()
        derecho = self.derecha.generacionCodigo()
        codigo += izquierdo
        codigo += derecho
        codigo += "POP ebx\n"
        codigo += "POP ecx\n"

        codigo += "SUBB ebx,ecx\n"
        codigo += "SUBB ebx,ecx\n"
        codigo += "PUSH 1\n"
        codigo += "PUSH -1\n"
        return codigo


# Fin Expresiones
#################################################################

# Sentencias
#################################################################


class Bloque(Nodo):
    """docstring for Bloque"""
    def __init__(self):
        super(Bloque, self).__init__()
        self.sentencia = None

    def inicializar(self, pila):
        pila.pop()
        pila.pop()
        pila.pop()
        self.sentencia = pila.pop().nodo
        pila.pop()
        pila.pop()
        # pila.pop()

        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Bloque>".format(tabulaciones))
        self.sentencia.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.sentencia is None):
            self.sentencia.decideTipo()
            if self.sentencia.tipo_dato != "e":
                self.tipo_dato = "v"
        else:
            self.tipo_dato = "v"

    # Pendiente
    def generacionCodigo(self):
        codigo = ""
        codigo += self.sentencia.generacionCodigo()
        return codigo


class ValorRegresa(Expresion):
    """docstring for SentenciaBloque"""
    def __init__(self):
        super(ValorRegresa, self).__init__()
        self.expresion = None

    def inicializar(self, pila):
        pila.pop()
        self.expresion = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<ValorRegresa>".format(tabulaciones))
        if not (self.expresion is None):
            self.expresion.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        if not (self.expresion is None):
            self.expresion.decideTipo()
            if self.expresion.tipo_dato != "e":
                self.tipo_dato = self.expresion.tipo_dato
            else:
                raise Errores(
                    "EL retorno no es el correcto en el ambito {0}".format(
                        Globales.ambito))
        else:
            self.tipo_dato = "v"

    # Pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.expresion is None):
            codigo += self.expresion.generacionCodigo()
            codigo += "POP eax\n"
            codigo += "PUSH eax\n"
        return codigo


class Sentencia(Nodo):
    """docstring for Sentencia"""
    def __init__(self):
        super(Sentencia, self).__init__()
        self.llamada_funcion = None

    def inicializar(self, pila):
        pila.pop()
        pila.pop()
        pila.pop()
        self.llamada_funcion = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Sentencia>".format(tabulaciones))
        self.llamada_funcion.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        self.llamada_funcion.decideTipo()

        if self.llamada_funcion.tipo_dato != "e":
            self.tipo_dato = self.llamada_funcion.tipo_dato
        else:
            raise Errores(
                "El tipo de dato no es el correcto en la llamada a funcion {0} en el ambito {1}"
                .format(self.llamada_funcion.identificador.simbolo,
                        Globales.ambito))

    # Pendiente
    def generacionCodigo(self):
        codigo = ""
        codigo += self.llamada_funcion.generacionCodigo()
        return codigo


class Asignacion(Nodo):
    """docstring for Igualdad"""
    def __init__(self):
        super(Asignacion, self).__init__()
        self.expresion = None
        self.identificador = Identificador()
        self.operador = None

    def inicializar(self, pila):
        pila.pop()
        pila.pop()
        pila.pop()
        self.expresion = pila.pop().nodo
        pila.pop()
        self.operador = pila.pop().terminal
        pila.pop()
        self.identificador.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Igualdad>".format(tabulaciones))
        self.identificador.imprimir(tabulaciones + "\t")
        print("{0}{1}".format(tabulaciones, self.operador))
        self.expresion.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        # revisar identificador en tabla simbolos

        self.identificador.decideTipo()
        self.expresion.decideTipo()

        if self.identificador.tipo_dato != "e" and self.identificador.tipo_dato == self.expresion.tipo_dato:
            self.tipo_dato = self.identificador.tipo_dato
        else:
            raise Errores(
                "Los tipos de datos no coinciden en la asignacion del identificador {0} en el ambito {1}"
                .format(self.identificador.simbolo, Globales.ambito))

    def generacionCodigo(self):
        codigo = ""
        expresion = ""
        expresion += self.expresion.generacionCodigo()
        codigo += expresion
        codigo += "POP eax\n"
        codigo += "MOV {0}, eax\n".format(self.identificador.simbolo)
        return codigo


class ListaParametros(Nodo):
    """docstring for ListaParametros"""
    def __init__(self):
        super(ListaParametros, self).__init__()
        self.lista_parametros = None
        self.identificador = Identificador()
        self.tipo = None

    def inicializar(self, pila):
        pila.pop()
        self.lista_parametros = pila.pop().nodo
        pila.pop()
        self.identificador.simbolo = pila.pop().terminal
        pila.pop()
        self.tipo = Tipo(pila.pop().terminal)
        pila.pop()
        pila.pop()
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<ListaParametros>".format(tabulaciones))
        if not (self.tipo is None):
            self.tipo.imprimir(tabulaciones)
            self.identificador.imprimir(tabulaciones)
            # print("{0}<Identificador>\n{1}".format(tabulaciones, self.identificador))
            self.lista_parametros.imprimir(tabulaciones)

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.tipo is None):
            self.tipo.decideTipo()
            self.identificador.decideTipo()

            if self.tipo.tipo_dato != "e" and self.identificador.tipo_dato == "e":
                if not (self.lista_parametros is None):
                    self.lista_parametros.decideTipo()
                    if self.lista_parametros.tipo_dato != "e":
                        self.tipo_dato = self.tipo.tipo_dato
                        Globales.tabla_simbolos.actualizarFuncion(
                            self.identificador.simbolo, self.tipo_dato)
                    else:
                        raise Errores(
                            "Los parametros tienen algo mal en el ambito {0}".
                            format(Globales.ambito))
                else:
                    self.tipo_dato = self.tipo.tipo_dato
                    Globales.tabla_simbolos.actualizarFuncion(
                        self.identificador.simbolo, self.tipo_dato)
            else:
                raise Errores(
                    "El parametro {0} en el ambito {1} ya existe".format(
                        self.identificador.simbolo, Globales.ambito))
        else:
            self.tipo_dato = "v"

    # pendiente
    def generacionCodigo(self):
        global tipos_ensamblador
        codigo = ""
        if not (self.tipo is None):
            codigo += "{0}: {1} ".format(self.identificador.simbolo,
                                         tipos_ensamblador.get(self.tipo_dato))
            if not (self.lista_parametros is None):
                codigo += self.lista_parametros.generacionCodigo()
        return codigo


class ListaArgumentos(Nodo):
    """docstring for ListaArgumentos"""
    def __init__(self):
        super(ListaArgumentos, self).__init__()
        self.expresion = None
        self.lista_argumentos = None

    def inicializar(self, pila):
        pila.pop()
        self.lista_argumentos = pila.pop().nodo
        pila.pop()
        self.expresion = pila.pop().nodo
        pila.pop()
        pila.pop()
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<ListaArgumentos>".format(tabulaciones))
        if not (self.expresion is None):
            self.expresion.imprimir(tabulaciones + "\t")
            self.lista_argumentos.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        pass

    def decideRecursivo(self, nombre_funcion, argumento, contador):
        self.tipo_dato = "e"
        funcion, pos = Globales.tabla_simbolos.buscaFuncion(nombre_funcion)

        if not (self.expresion is None):
            self.expresion.decideTipo()
            if self.expresion.tipo_dato == "v":
                if len(funcion.lista_parametros) == contador:
                    self.tipo_dato = "v"
            elif self.expresion.tipo_dato != "e" and len(
                    funcion.lista_parametros
            ) >= argumento and funcion.lista_parametros[
                    argumento].tipo == self.expresion.tipo_dato:

                self.lista_argumentos.decideRecursivo(nombre_funcion,
                                                      argumento - 1, contador + 1)
                if self.lista_argumentos.tipo_dato != "e":
                    self.tipo_dato = "v"
                else:
                    raise Errores(
                        "0 Los argumentos no coinciden en el ambito {0}".format(
                            Globales.ambito))
            else:
                raise Errores(
                    "1 Los argumentos no coinciden en el ambito {0}".format(
                        Globales.ambito))
        elif len(funcion.lista_parametros) == contador:
            self.tipo_dato = "v"
        else:
            raise Errores("2 Los argumentos no coinciden en el ambito {0}".format(
                Globales.ambito))

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.expresion is None):
            codigo += self.expresion.generacionCodigo()
            if not (self.lista_argumentos is None):
                codigo += self.lista_argumentos.generacionCodigo()
        return codigo


class ListaVariables(Nodo):
    """docstring for ListaVariables"""
    def __init__(self):
        super(ListaVariables, self).__init__()
        self.lista_variables = None
        self.identificador = Identificador()

    def inicializar(self, pila):
        pila.pop()
        self.lista_variables = pila.pop().nodo
        pila.pop()
        self.identificador.simbolo = pila.pop().terminal
        pila.pop()
        pila.pop()
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<ListaVariables>".format(tabulaciones))
        if not (self.identificador is None):
            self.identificador.imprimir(tabulaciones + "\t")
        if not (self.lista_variables is None):
            self.lista_variables.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        pass

    def decideRecursivo(self, tipo_daclarado):
        self.tipo_dato = "e"

        if not (self.identificador is None):
            self.identificador.decideTipo()
            if self.identificador.tipo_dato == "v":
                self.tipo_dato = "v"
            elif self.identificador.tipo_dato == "e":
                if not (self.lista_variables is None):
                    self.lista_variables.decideRecursivo(tipo_daclarado)

                    if self.lista_variables.tipo_dato != "e":
                        self.tipo_dato = tipo_daclarado
                        encontrado = Globales.tabla_simbolos.buscaIdentificador(
                            self.identificador.simbolo)
                        if len(encontrado) == 0:
                            Globales.tabla_simbolos.agregaVariable(
                                self.identificador.simbolo, tipo_daclarado)
                        else:
                            raise Errores(
                                "Variable {0} previamente definida en el ambito {1}"
                                .format(self.identificador.simbolo,
                                        Globales.ambito))
                    else:
                        raise Errores(
                            "Variable {0} previamente definida en el ambito {1}"
                            .format(self.identificador.simbolo,
                                    Globales.ambito))
                else:
                    self.tipo_dato = tipo_daclarado
                    encontrado = Globales.tabla_simbolos.buscaIdentificador(
                        self.identificador.simbolo)
                    if len(encontrado) == 0:
                        Globales.tabla_simbolos.agregaVariable(
                            self.identificador.simbolo, tipo_daclarado)
                    else:
                        raise Errores(
                            "Variable {0} previamente definida en el ambito {1}"
                            .format(self.identificador.simbolo,
                                    Globales.ambito))

            else:
                raise Errores(
                    "Variable {0} previamente definida en el ambito {1}".
                    format(self.identificador.simbolo, Globales.ambito))
        else:
            self.tipo_dato = "v"

    # pendiente
    def generacionCodigo(self):
        global tipos_ensamblador
        codigo = ""
        if Globales.ambito != "global" and not ( self.identificador is None) and self.identificador.simbolo != "":
            codigo += "local {0}: {1}\n".format( self.identificador.simbolo, tipos_ensamblador.get(self.tipo_dato))
            if not (self.lista_variables is None):
                codigo += self.lista_variables.generacionCodigo()
        return codigo


# Conflictos


class Definicion(Nodo):
    """docstring for Definicion"""
    def __init__(self):
        super(Definicion, self).__init__()
        self.definicion_funcion = None
        self.definicion_variable = None

    def definicioFuncion(self, pila):
        pila.pop()
        self.definicion_funcion = pila.pop().nodo
        return pila

    def definicionVariable(self, pila):
        pila.pop()
        self.definicion_variable = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Definicion>".format(tabulaciones))
        if not (self.definicion_funcion is None):
            # print("{0}Entro fun".format(tabulaciones))
            self.definicion_funcion.imprimir(tabulaciones + "\t")
        else:
            self.definicion_variable.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        checa = ""

        if not (self.definicion_funcion is None):
            self.definicion_funcion.decideTipo()
            checa += self.definicion_funcion.tipo_dato
        else:
            self.definicion_variable.decideTipo()
            checa += self.definicion_variable.tipo_dato

        if checa != "e":
            self.tipo_dato = "v"
        else:
            raise Errores(
                "La definicion en el ambito {0} es incorrectas".format(
                    Globales.ambito))

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.definicion_funcion is None):
            codigo += self.definicion_funcion.generacionCodigo()
        else:
            codigo += self.definicion_variable.generacionCodigo()
        return codigo


class DefinicionLocal(Nodo):
    """docstring for DefinicionLocal"""
    def __init__(self):
        super(DefinicionLocal, self).__init__()
        self.sentencia = None
        self.definicion_variable = None

    def definicionSentencia(self, pila):
        pila.pop()
        self.sentencia = pila.pop().nodo
        return pila

    def definicionVariable(self, pila):
        pila.pop()
        self.definicion_variable = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<DefinicionLocal>".format(tabulaciones))
        if not (self.sentencia is None):
            self.sentencia.imprimir(tabulaciones + "\t")
        else:
            self.definicion_variable.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        checa = ""
        self.tipo_dato = "e"

        if not (self.sentencia is None):
            self.sentencia.decideTipo()
            checa += self.sentencia.tipo_dato
        else:
            self.definicion_variable.decideTipo()
            checa += self.definicion_variable.tipo_dato

        if checa != "e":
            self.tipo_dato = "v"
        else:
            raise Errores(
                "La definicion local en el ambito {0} son incorrectas".format(
                    Globales.ambito))

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.sentencia is None):
            codigo += self.sentencia.generacionCodigo()
        else:
            codigo += self.definicion_variable.generacionCodigo()
        return codigo


class SentenciaBloque(Nodo):
    """docstring for SentenciaBloque"""
    def __init__(self):
        super(SentenciaBloque, self).__init__()
        self.sentencia = None
        self.bloque = None

    def definicionSentencia(self, pila):
        pila.pop()
        self.sentencia = pila.pop().nodo
        return pila

    def definicionBloque(self, pila):
        pila.pop()
        self.bloque = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<SentenciaBloque>".format(tabulaciones))
        if not (self.sentencia is None):
            self.sentencia.imprimir(tabulaciones + "\t")
        else:
            self.bloque.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        checa = ""
        if not (self.sentencia is None):
            self.sentencia.decideTipo()
            checa = self.sentencia.tipo_dato
        else:
            self.bloque.decideTipo()
            checa = self.bloque.tipo_dato

        if checa != "e":
            self.tipo_dato = "v"
        else:
            raise Errores(
                "Las sentencias de bloque en el ambito {0} son incorrectas".
                format(Globales.ambito))

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.sentencia is None):
            codigo += self.sentencia.generacionCodigo()
        else:
            codigo += self.bloque.generacionCodigo()
        return codigo


# Conflictos


class Definiciones(Nodo):
    """docstring for Definiciones"""
    def __init__(self):
        super(Definiciones, self).__init__()
        self.definiciones = None
        self.definicion = None

    def inicializar(self, pila):
        pila.pop()
        self.definiciones = pila.pop().nodo
        pila.pop()
        self.definicion = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Definiciones>".format(tabulaciones))
        if not (self.definicion is None):
            self.definicion.imprimir(tabulaciones + "\t")
            self.definiciones.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        if not (self.definicion is None):
            self.definicion.decideTipo()
            if not (self.definiciones is None):
                self.definiciones.decideTipo()
                if self.definicion.tipo_dato != "e" and self.definiciones.tipo_dato != "e":
                    self.tipo_dato = "v"
                else:
                    raise Errores(
                        "0 Las definiciones en el ambito {0} son incorrectas".
                        format(Globales.ambito))
            else:
                if self.definicion.tipo_dato != "e":
                    self.tipo_dato = "v"
                else:
                    raise Errores(
                        "1 Las definiciones en el ambito {0} son incorrectas".
                        format(Globales.ambito))
        else:
            self.tipo_dato = "v"

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.definicion is None):
            codigo += self.definicion.generacionCodigo()
            if not (self.definiciones is None):
                codigo += self.definiciones.generacionCodigo()
        return codigo


##############################################################


class Sentencias(Nodo):
    """docstring for Sentencias"""
    def __init__(self):
        super(Sentencias, self).__init__()
        self.sentencias = None
        self.sentencia = None

    def inicializar(self, pila):
        pila.pop()
        self.sentencias = pila.pop().nodo
        pila.pop()
        self.sentencia = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Sentencias>".format(tabulaciones))
        if not (self.sentencia is None):
            self.sentencia.imprimir(tabulaciones + "\t")
            self.sentencias.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.sentencia is None):
            self.sentencia.decideTipo()
            if not (self.sentencias is None):
                self.sentencias.decideTipo()
                if self.sentencia.tipo_dato != "e" and self.sentencias.tipo_dato != "e":
                    self.tipo_dato = "v"
                else:
                    raise Errores(
                        "0 Las sentencias en el ambito {0} son incorrectas".
                        format(Globales.ambito))
            elif self.sentencia.tipo_dato != "e":
                self.tipo_dato = "v"
            else:
                raise Errores(
                    "1 Las sentencias en el ambito {0} son incorrectas".format(
                        Globales.ambito))
        else:
            self.tipo_dato = "v"

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.sentencia is None):
            codigo += self.sentencia.generacionCodigo()
            if not (self.sentencias is None):
                codigo += self.sentencias.generacionCodigo()
        return codigo


class DefinicionesLocales(Nodo):
    """docstring for DefinicionesLocales"""
    def __init__(self):
        super(DefinicionesLocales, self).__init__()
        self.definiciones_locales = None
        self.definicion_local = None

    def inicializar(self, pila):
        pila.pop()
        self.definiciones_locales = pila.pop().nodo
        pila.pop()
        self.definicion_local = pila.pop().nodo
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<DefinicionesLocales>".format(tabulaciones))
        if not (self.definicion_local is None):
            self.definicion_local.imprimir(tabulaciones + "\t")
            self.definiciones_locales.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.definicion_local is None):
            self.definicion_local.decideTipo()
            if not (self.definiciones_locales is None):
                self.definiciones_locales.decideTipo()

                if self.definicion_local.tipo_dato != "e" and self.definiciones_locales.tipo_dato != "e":
                    self.tipo_dato = "v"
                else:
                    raise Errores(
                        "0 Las definiciones locales en el ambito {0} son incorrectas"
                        .format(Globales.ambito))
            elif self.definicion_local.tipo_dato != "e":
                self.tipo_dato = "v"
            else:
                raise Errores(
                    "1 Las definiciones locales en el ambito {0} son incorrectas"
                    .format(Globales.ambito))
        else:
            self.tipo_dato = "v"

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.definicion_local is None):
            codigo += self.definicion_local.generacionCodigo()
            if not (self.definiciones_locales is None):
                codigo += self.definiciones_locales.generacionCodigo()
        return codigo


class BloqueFuncion(Nodo):
    """docstring for BloqueFuncion"""
    def __init__(self):
        super(BloqueFuncion, self).__init__()
        self.definiciones_locales = None

    def inicializar(self, pila):
        pila.pop()
        pila.pop()
        pila.pop()
        self.definiciones_locales = pila.pop().nodo
        pila.pop()
        pila.pop()
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<BloqueFuncion>".format(tabulaciones))
        self.definiciones_locales.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.definiciones_locales is None):
            self.definiciones_locales.decideTipo()
            if self.definiciones_locales.tipo_dato != "e":
                self.tipo_dato = "v"
            else:
                raise Errores(
                    "0 El bloque de funcion en el ambito {0} son incorrectas".
                    format(Globales.ambito))
        else:
            raise Errores(
                "1 El bloque de funcion en el ambito {0} son incorrectas".
                format(Globales.ambito))

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        codigo += self.definiciones_locales.generacionCodigo()
        return codigo


class Parametros(Nodo):
    """docstring for Parametros"""
    def __init__(self):
        super(Parametros, self).__init__()
        self.lista_parametros = None
        self.identificador = Identificador()
        self.tipo = None

    def inicializar(self, pila):
        pila.pop()
        self.lista_parametros = pila.pop().nodo
        pila.pop()
        self.identificador.simbolo = pila.pop().terminal
        pila.pop()
        self.tipo = Tipo(pila.pop().terminal)
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Parametros>".format(tabulaciones))
        if not (self.tipo is None):
            self.tipo.imprimir(tabulaciones + "\t")
            self.identificador.imprimir(tabulaciones + "\t")
            self.lista_parametros.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.tipo is None):
            self.tipo.decideTipo()
            self.identificador.decideTipo()

            if self.tipo.tipo_dato != "e" and self.identificador.tipo_dato == "e":
                if not (self.lista_parametros is None):
                    self.lista_parametros.decideTipo()
                    if self.lista_parametros.tipo_dato != "e":
                        self.tipo_dato = self.tipo.tipo_dato
                        Globales.tabla_simbolos.actualizarFuncion(
                            self.identificador.simbolo, self.tipo_dato)
                else:
                    self.tipo_dato = self.tipo.tipo_dato
                    Globales.tabla_simbolos.actualizarFuncion(
                        self.identificador.simbolo, self.tipo_dato)
            else:
                raise Errores(
                    "Los parametros en el ambito {0} son incorrectas".format(
                        Globales.ambito))
        else:
            self.tipo_dato = "v"

    # pendiente
    def generacionCodigo(self):
        global tipos_ensamblador
        codigo = ""
        if not (self.tipo is None):
            codigo += "{0}: {1} ".format(self.identificador.simbolo,
                                         tipos_ensamblador.get(self.tipo_dato))
            if not (self.lista_parametros is None):
                codigo += self.lista_parametros.generacionCodigo()
        return codigo


class DefinicionFuncion(Nodo):
    """docstring for DefinicionFuncion"""
    def __init__(self):
        super(DefinicionFuncion, self).__init__()
        self.bloque_funcion = None
        self.parametros = None
        self.identificador = Identificador()
        self.tipo = None

    def inicializar(self, pila):
        pila.pop()
        self.bloque_funcion = pila.pop().nodo
        pila.pop()
        pila.pop()
        pila.pop()
        self.parametros = pila.pop().nodo
        pila.pop()
        pila.pop()
        pila.pop()
        self.identificador.simbolo = pila.pop().terminal
        pila.pop()
        self.tipo = Tipo(pila.pop().terminal)
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<DefinicionFuncion>".format(tabulaciones))

        self.tipo.imprimir(tabulaciones)
        self.identificador.imprimir(tabulaciones + "\t")
        self.parametros.imprimir(tabulaciones + "\t")
        self.bloque_funcion.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        self.tipo.decideTipo()
        self.identificador.decideTipo()

        if self.identificador.tipo_dato == "e" and self.tipo.tipo_dato != "e":

            self.tipo_dato = self.tipo.tipo_dato
            Globales.tabla_simbolos.agregaFuncion(self)
            Globales.cambioAmbito(self.identificador.simbolo)

            if not (self.parametros is None):
                self.parametros.decideTipo()
                self.bloque_funcion.decideTipo()

                if self.parametros.tipo_dato != "e" and self.bloque_funcion.tipo_dato != "e":
                    if Globales.tipo_retorno == self.tipo.tipo_dato:
                        self.tipo_dato = self.tipo.tipo_dato
                        Globales.regresaAmbito()
                        Globales.tipo_retorno = "v"
                    else:
                        raise Errores(
                            "0 No coincide el tipo de retorno de la funcion {0}"
                            .format(self.identificador.simbolo))
            else:
                self.bloque_funcion.decideTipo()
                if self.bloque_funcion.tipo_dato != "e":
                    if Globales.tipo_retorno == self.tipo.tipo_dato:
                        self.tipo_dato = self.tipo.tipo_dato
                        Globales.regresaAmbito()
                        # Globales.tabla_simbolos.agregaFuncion(self)
                        Globales.tipo_retorno = "v"
                    else:
                        raise Errores(
                            "1 No coincide el tipo de retorno de la funcion {0}"
                            .format(self.identificador.simbolo))
                else:
                    raise Errores(
                        "El bloque de funcion de la funcion {0} es incorrectas"
                        .format(self.identificador.simbolo))

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        Globales.cambioAmbito(self.identificador.simbolo)
        codigo += "proc {0} {1}".format(self.identificador.simbolo,
                                        self.parametros.generacionCodigo())
        codigo += self.bloque_funcion.generacionCodigo()
        codigo += "{0} endp\n\n".format(self.identificador.simbolo)
        Globales.regresaAmbito()
        Globales.tipo_retorno = "v"
        return codigo


class DefinicionVariable(Nodo):
    """docstring for DefinicionVariable"""
    def __init__(self):
        super(DefinicionVariable, self).__init__()
        self.lista_variables = None
        self.identificador = Identificador()
        self.tipo = None

    def inicializar(self, pila):
        pila.pop()
        pila.pop()
        pila.pop()
        self.lista_variables = pila.pop().nodo
        pila.pop()
        self.identificador.simbolo = pila.pop().terminal
        pila.pop()
        self.tipo = Tipo(pila.pop().terminal)
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<DefinicionVariable>".format(tabulaciones))
        self.tipo.imprimir(tabulaciones)
        self.identificador.imprimir(tabulaciones + "\t")
        self.lista_variables.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        self.tipo.decideTipo()
        self.identificador.decideTipo()

        if self.tipo.tipo_dato != "e" and self.identificador.tipo_dato == "e":

            encontrado = Globales.tabla_simbolos.buscaIdentificador(
                self.identificador.simbolo)

            if not (self.lista_variables is None):
                self.lista_variables.decideRecursivo(self.tipo.tipo_dato)
                if self.lista_variables.tipo_dato != "e":
                    self.tipo_dato = self.tipo.tipo_dato
                    if len(encontrado) == 0:
                        Globales.tabla_simbolos.agregaVariable(
                            self.identificador.simbolo, self.tipo_dato)
                    else:
                        raise Errores(
                            "Variable {0} previamente definida en el ambito {1}"
                            .format(self.identificador.simbolo,
                                    Globales.ambito))
            else:
                self.tipo_dato = self.tipo.tipo_dato
                # encontrado = Globales.tabla_simbolos.buscaIdentificador(self.identificador.simbolo)
                if len(encontrado) == 0:
                    Globales.tabla_simbolos.agregaVariable(
                        self.identificador.simbolo, self.tipo_dato)
                else:
                    raise Errores(
                        "Variable {0} previamente definida en el ambito {1}".
                        format(self.identificador.simbolo, Globales.ambito))
        else:
            raise Errores(
                "Variable {0} previamente definida en el ambito {1}".format(
                    self.identificador.simbolo, Globales.ambito))

    # pendiente
    def generacionCodigo(self):
        global tipos_ensamblador
        codigo = ""
        if Globales.ambito != "global":
            codigo += "\nlocal {0}: {1}\n".format(
                self.identificador.simbolo,
                tipos_ensamblador.get(self.tipo_dato))
            if not (self.lista_variables is None):
                codigo += self.lista_variables.generacionCodigo()
        return codigo


class Argumentos(Nodo):
    """docstring for Argumentos"""
    def __init__(self):
        super(Argumentos, self).__init__()
        self.expresion = None
        self.lista_argumentos = None

    def inicializar(self, pila):
        pila.pop()
        self.lista_argumentos = pila.pop().nodo
        pila.pop()
        self.expresion = pila.pop().nodo

        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Argumentos>".format(tabulaciones))
        if not (self.expresion is None):
            self.expresion.imprimir(tabulaciones + "\t")
            self.lista_argumentos.imprimir(tabulaciones + "\t")

    # Pendiente
    def decideTipo(self):
        pass

    def decideRecursivo(self, nombre_funcion):
        self.tipo_dato = "e"
        funcion, pos = Globales.tabla_simbolos.buscaFuncion(nombre_funcion)

        if not (self.expresion is None):
            self.expresion.decideTipo()
            if self.expresion.tipo_dato == "v" and len(
                    funcion.lista_parametros) == 0:
                self.tipo_dato = "v"
            elif self.expresion.tipo_dato != "e" and funcion.lista_parametros[
                    -1].tipo == self.expresion.tipo_dato:
                if not (self.lista_argumentos is None):

                    self.lista_argumentos.decideRecursivo(
                        nombre_funcion, -2, 1)

                    if self.lista_argumentos.tipo_dato != "e":
                        self.tipo_dato = "v"
                    else:
                        raise Errores(
                            "0 Los argumentos de la funcion {0} en el ambito {1} son incorrectos"
                            .format(nombre_funcion, Globales.ambito))
                elif len(funcion.lista_parametros) == 1:
                    self.tipo_dato = "v"
                else:
                    raise Errores(
                        "1 Los argumentos de la funcion {0} en el ambito {1} son incorrectos"
                        .format(nombre_funcion, Globales.ambito))
            else:
                raise Errores(
                    "2 Los argumentos de la funcion {0} en el ambito {1} son incorrectos"
                    .format(nombre_funcion, Globales.ambito))
        elif len(funcion.lista_parametros) == 0:
            self.tipo_dato = "v"
        else:
            raise Errores(
                "3 Los argumentos de la funcion {0} en el ambito {1} son incorrectos"
                .format(nombre_funcion, Globales.ambito))

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.expresion is None):
            codigo += self.expresion.generacionCodigo()
            if not (self.lista_argumentos is None):
                codigo += self.lista_argumentos.generacionCodigo()
        codigo += "\n"
        return codigo


# Control Flujo
#################################################################


class CondicionalSimple(Sentencia):
    """docstring for CondicionalSimple"""
    def __init__(self):
        super(CondicionalSimple, self).__init__()
        self.otro = None
        self.expresion = None

    def inicializar(self, pila):
        pila.pop()
        self.otro = pila.pop().nodo
        pila.pop()
        self.sentencia_bloque = pila.pop().nodo
        pila.pop()
        pila.pop()
        pila.pop()
        self.expresion = pila.pop().nodo
        pila.pop()
        pila.pop()
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<CondicionalSimple>".format(tabulaciones))
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.expresion.imprimir(tabulaciones + "\t")
        self.sentencia_bloque.imprimir(tabulaciones + "\t")
        self.otro.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        nuevo_ambito = Globales.agregaCondicionSimple()
        Globales.cambioAmbito(nuevo_ambito)

        self.expresion.decideTipo()

        if self.expresion.tipo_dato != "e":
            self.sentencia_bloque.decideTipo()

            if self.sentencia_bloque.tipo_dato != "e":
                if not (self.otro is None):
                    self.otro.decideTipo()

                    if self.otro.tipo_dato != "e":
                        self.tipo_dato = "v"
                else:
                    self.tipo_dato = "v"
            else:
                raise Errores(
                    "En las sentencias del if en el ambito {0}".format(
                        Globales.ambito))
        else:
            raise Errores(
                "Los tipos de datos no coinciden en la comparacion del if en el ambito {0}"
                .format(Globales.ambito))
        Globales.regresaAmbito()

    # pendiente
    def generacionCodigo(self):
        # return self.sentencia.generacionCodigo()
        global inversiones
        codigo = "\n"
        if not (self.sentencia_bloque is None):
            etiqueta_inicio = Globales.agregaCondicionSimple()
            etiqueta_fin = Globales.finCondicionSimple()

            codigo += "{0}: \n{1}".format(etiqueta_inicio,
                                          self.expresion.generacionCodigo())
            codigo += "POP eax\n"
            codigo += "CMP eax, 1\n"
            codigo += "JL {0}\n".format(etiqueta_fin)
            codigo += self.sentencia_bloque.generacionCodigo()
            codigo += "{0}:\n".format(etiqueta_fin)

            if not (self.otro is None):
                codigo_otro = self.otro.generacionCodigo()
                if codigo_otro != "":
                    codigo += codigo_otro
        return codigo


class Mientras(Sentencia):
    """docstring for Mientras"""
    def __init__(self):
        super(Mientras, self).__init__()
        self.expresion = None
        self.bloque = None

    def inicializar(self, pila):
        pila.pop()
        self.bloque = pila.pop().nodo
        pila.pop()
        pila.pop()
        pila.pop()
        self.expresion = pila.pop().nodo
        pila.pop()
        pila.pop()
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Mientras>".format(tabulaciones))
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.expresion.imprimir(tabulaciones + "\t")
        self.bloque.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"
        nuevo_ambito = Globales.agregaMientras()
        Globales.cambioAmbito(nuevo_ambito)

        self.expresion.decideTipo()

        if self.expresion.tipo_dato != "e":
            self.bloque.decideTipo()

            if self.bloque.tipo_dato != "e":
                self.tipo_dato = "v"
            else:
                raise Errores(f"Las sentencias del while en el ambito {Globales.ambito} son incorrectas")
        else:
            raise Errores(f"Los tipos de datos no coinciden en la comparacion en el while en el ambito {Globales.ambito}")
        Globales.regresaAmbito()

    # pendiente
    def generacionCodigo(self):
        # return self.sentencia.generacionCodigo()
        global inversiones
        codigo = "\n"
        if not (self.bloque is None):
            etiqueta_inicio = Globales.agregaMientras()
            etiqueta_fin = Globales.finMientras()

            codigo += "{0}: \n{1}".format(etiqueta_inicio,
                                          self.expresion.generacionCodigo())
            codigo += "POP eax\n"
            codigo += "CMP eax, 1\n"
            codigo += "JL {0}\n".format(etiqueta_fin)
            codigo += self.bloque.generacionCodigo()
            codigo += "JMP {0}\n".format(etiqueta_inicio)
            codigo += "{0}:\n".format(etiqueta_fin)
        return codigo


class Retorno(Sentencia):
    """docstring for Expresion"""
    def __init__(self):
        super(Retorno, self).__init__()
        self.valor_regresa = None

    def inicializar(self, pila):
        pila.pop()
        pila.pop()
        pila.pop()
        self.valor_regresa = pila.pop().nodo
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<Retorno>".format(tabulaciones))
        print("{0}{1}".format(tabulaciones, self.simbolo))
        self.valor_regresa.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.valor_regresa is None):
            self.valor_regresa.decideTipo()
            if self.valor_regresa.tipo_dato != "e":
                self.tipo_dato = self.valor_regresa.tipo_dato
                Globales.tipo_retorno = self.tipo_dato
            else:
                raise Errores(f"El valor de retorno en el ambito {Globales.ambito} es incorrecto")
        else:
            self.tipo_dato = "v"
            Globales.tipo_retorno = self.tipo_dato

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if self.tipo_dato != "v":
            codigo += self.valor_regresa.generacionCodigo()
            codigo += "ret\n"
        elif not (self.valor_regresa is None):
            codigo += "ret\n"
        return codigo


class CondicionalCompuesta(Sentencia):
    """docstring for Expresion"""
    def __init__(self):
        super(CondicionalCompuesta, self).__init__()
        self.sentencia_bloque = None

    def inicializar(self, pila):
        pila.pop()
        self.sentencia_bloque = pila.pop().nodo
        pila.pop()
        self.simbolo = pila.pop().terminal
        return pila

    def imprimir(self, tabulaciones):
        print("{0}<CondicionalCompuesta>".format(tabulaciones))
        if not (self.simbolo != ""):
            print("{0}{1}".format(tabulaciones, self.simbolo))
            self.sentencia_bloque.imprimir(tabulaciones + "\t")

    def decideTipo(self):
        self.tipo_dato = "e"

        if not (self.sentencia_bloque is None):
            nuevo_ambito = Globales.agregaCondicionDoble()
            Globales.cambioAmbito(nuevo_ambito)
            self.sentencia_bloque.decideTipo()
            if self.sentencia_bloque.tipo_dato != "e":
                self.tipo_dato = "v"
            else:
                raise Errores(
                    "Los tipos de datos no coinciden en las sentencias del else en el ambito {0}"
                    .format(Globales.ambito))
            Globales.regresaAmbito()
        else:
            self.tipo_dato = "v"

    # pendiente
    def generacionCodigo(self):
        codigo = ""
        if not (self.sentencia_bloque is None):
            codigo += self.sentencia_bloque.generacionCodigo()
        return codigo


# Fin Control Flujo
#################################################################
