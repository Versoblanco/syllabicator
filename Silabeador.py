#coding=UTF-8
# División silábica en español (Quilis, Tratado de fonética y fonología, p. 368 y ss.)
# V=vocal C = consonante.
# 1. VCV = V-CV
# 2. VCCV = a) VC-CV b) V-CCV (p, b, f, g, k + r, l / dr, tr)
# 3. VCCC(C)V = a)VCC (ns, bs) - CV b)VC-CCV (C + l, r) cons- truir an-sie-dad
# 4. VV = a) V-V (abiertas, abierta + cerrada tónica, cerrada tónica + abierta) b) VV (cerradas, abierta+cerrada átona, cerrada átona + abierta)
# La consonante no puede ser núcleo ni constituir sílaba por sí misma (salvo semiconsonante y)
# prefijos = sub


def definir_alfabeto():
    consonantes = map(lambda word: unicode(word, 'utf-8'),
                      ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w',
                       'x', 'y', 'z'])
    vocales = map(lambda word: unicode(word, 'utf-8'), ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü'])
    alfabeto = consonantes+ vocales
    return alfabeto

def validar_letra(caracter):
    alfabeto = definir_alfabeto()
    if caracter in alfabeto:
        return caracter
    else:
        return ''

def es_vocal(letra):
    vocales =map(lambda word: unicode(word, 'utf-8'), ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü'])
    return letra in vocales


def es_consonante(letra):
    consonantes =  map(lambda word: unicode(word, 'utf-8'), ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    return letra in consonantes


def es_inseparable(letra1, letra2):
    inseparables = map(lambda word: unicode(word, 'utf-8'),
                       ['ch', 'll', 'rr', 'pr', 'pl', 'br', 'bl', 'fr', 'fl', 'gr', 'gl', 'kr', 'cr', 'kl', 'cl', 'dr',
                        'tr'])
    if not letra1 or not letra2:
        return False
    return letra1+letra2 in inseparables

def es_diptongo(letra1, letra2):
    vcerradas = map(lambda word: unicode(word, 'utf-8'), ['i', 'u', 'ü'])
    return letra1 in vcerradas or letra2 in vcerradas

def buscar_letra_anterior(palabra, index):
    return palabra[index-1]

def buscar_letra_siguiente(palabra, index):
    if index == len(palabra)-1:
        return False
    else:
        return palabra[index+1]

def buscar_letra_consiguiente(palabra, index):
    if index >= len(palabra)-2:
        return False
    else:
        return palabra[index+2]

def pedir_palabra():
    while True:
        palabra = raw_input('Escriba la palabra (exit para salir): ').decode('utf-8').strip()
        if palabra == 'exit':
            print 'Adiós'
            exit()
        if len(palabra) > 0:
            return palabra


def dar_formato(palabra):
    palabra = palabra.lower()
    palabra = ''.join(map(validar_letra, palabra))
    return palabra

def silabear(palabra):

    silaba = ''
    silabeo = []

    for index, letra in enumerate(palabra):

        letra_anterior = buscar_letra_anterior(palabra, index)
        letra_siguiente = buscar_letra_siguiente(palabra, index)
        letra_consiguiente = buscar_letra_consiguiente(palabra, index)

        if index==0:
            silaba=letra
            continue

        elif es_vocal(letra) and es_consonante(letra_anterior):           # Estructura CV, la vocal se agrupa siempre con la consonante
            silaba=silaba+letra

        elif es_vocal(letra) and es_vocal(letra_anterior):                     # Estructura VV

            if es_diptongo(letra_anterior, letra):                                       # Diptongo VV, cuando una de las vocales es cerrada átona (i, u), resto de casos forma hiato V-V
                silaba=silaba+letra
            else:
                silabeo.append(silaba)
                silaba = letra

        elif es_consonante(letra):                                                        #Estructuras C(C)V, C(C)C, V(C)V, V(C)C

            if es_inseparable(letra, letra_siguiente) and es_vocal(letra_consiguiente):
                silabeo.append(silaba)
                silaba = letra
            elif not es_inseparable(letra_anterior, letra) and es_vocal(letra_siguiente):
                silabeo.append(silaba)
                silaba = letra
            else:
                silaba=silaba+letra

        else:
            print 'Error'
            break
    silabeo.append(silaba)
    return silabeo

def silabeador():
    while True:
        palabra = pedir_palabra()
        palabra = dar_formato(palabra)
        silabeo = silabear(palabra)
        silabeo = '-'.join(silabeo)
        print silabeo


silabeador()