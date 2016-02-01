# -*- ENCODING: UTF-8 -*-
"""
 * File:   Globales.py
 * Authors: Arellano Gonzalez Claudia Karina
 *          Miguel Ochoa Hernandez
 *
"""

from Componentes.TablaSimbolos import *

__author__ = "Arellano Gonzalez Claudia Karina, Miguel Ochoa Hernandez"

tabla_simbolos = TablaSimbolos()
ambito = "global"
ambitos_anteriores = []
mientras = -1
condicion_simple = -1
condicion_doble = -1
tipo_retorno = "v"


def reiniciar():
    global ambito
    global ambitos_anteriores
    global mientras
    global condicion_simple
    global condicion_doble
    global tipo_retorno

    ambito = "global"
    tipo_retorno = "v"
    ambitos_anteriores = []
    mientras = -1
    condicion_simple = -1
    condicion_doble = -1
    pass

def agregaMientras():
    global mientras
    mientras += 1
    return "WHILE{0}".format(mientras)
    pass

def agregaCondicionSimple():
    global condicion_simple
    condicion_simple += 1
    return "IF{0}".format(condicion_simple)
    pass

def finMientras():
    global mientras
    return "ENDIFMIENTRAS{0}".format(mientras)
    pass

def finCondicionSimple():
    global condicion_simple
    return "ENDIF{0}".format(condicion_simple)
    pass

def agregaCondicionDoble():
    global condicion_doble
    condicion_doble += 1
    return "ELSE{0}".format(condicion_doble)
    pass

def cambioAmbito(nuevo_ambito):
    global ambito
    global ambitos_anteriores

    ambitos_anteriores.append(ambito)
    ambito = nuevo_ambito
    pass

def regresaAmbito():
    global ambito
    global ambitos_anteriores
    ambito = ambitos_anteriores.pop()
    pass

def totalIdentificadores():
    encontrado = False
    revisar_ambitos = []

    for i in range(0, len(Globales.ambitos_anteriores)):
        revisar_ambitos.append(Globales.ambitos_anteriores[i])
        pass
    revisar_ambitos.append(Globales.ambito)

    while len(revisar_ambitos) > 0 and not encontrado:
        ambito_actual = revisar_ambitos.pop()
        posicion = Globales.tabla_simbolos.hash(ambito_actual)
        variables_en_ambito = Globales.tabla_simbolos.tabla[posicion]
        print("ambito {0}".format(ambito_actual))
        for j in variables_en_ambito:
            print("Identificador actual {0} con tipo {1}".format(j.simbolo, j.tipo))
            # print("Identificador buscado {0}".format(simbolo))
            pass
        pass
    pass

def totalAmbitos():
    global ambitos_anteriores
    global ambito
    print("\nTotal de ambitos")
    print("actual {0}".format(ambito))
    for i in ambitos_anteriores:
        print(i)
        pass
    pass