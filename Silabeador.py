#coding=UTF-8

# La funcionalidad está creada para la división silábica normativa de unidades discretas del español (conjuntos silábico, palabras y pseudopalabras). No es aplicable a la transcripción fonética ni el análisis métrico del verso.

# Se aplica, adaptado a ortografía del español, la división silábica expuesta en Quilis, Tratado de fonética y fonología, p. 368 y ss.

# La consonante no puede ser núcleo ni constituir sílaba por sí misma.

# Las semivocales 'y, w' y la letra hache son tratadas como consonantes, por lo que algunas palabras, especialmente los extranjerismos, diferirán de la segmentación más adecuada, otros casos se acercan a lo que un hispanohablante diría si desconoce la fonética del idioma - 'w-his-key', 'billy', 's-pain', 've-ge-ta-ble', 'a-mat-xu'

# Algunos prefijos ('sub', 'psi' o 'pso') producen errores 'su-bín-dice*', 'pa-rap-si-có-lo-go*', 'p-so-ria-sis*', estos elementos no siguen la regla general al percibirse como una unidad independiente cuya identidad de sentido se prioriza sobre el uso fonético, si bien existen casos límite donde el prefijo está prácticamente lexicalizado 'su-bra-yar / sub-ra-yar'. Esto no ocurre con otras palabras o pseudopalabras donde por no percibirse esa unidad el hispanohablante siempre agrupa la consonante con la vocal que le sigue: 'rap-so-da', 'pep-si', 'su-bli-me'

#   V=vocal C = consonante.

#   1. VCV =      V-CV 'a-mo'

#   2. VCCV =     a) VC-CV 'ar-mo'
#                 b) V-CCV 'a-bro' [(b, c, f, g, k, p) + (l, r), dr, tr, ch, ll, rr]

#   3. VCCC(C)V = a)VCC (ns, bs) - (C)CV 'ins-tante', 'obs- truir'
#                 b)VC-CCV 'in-tra' (grupo inseparable)

#   4. VV =       a) V-V 've-a', 'le-í-a' (abiertas, abierta + cerrada tónica, cerrada tónica + abierta)
#                 b) VV 'au-ra' (cerradas, abierta+cerrada átona, cerrada átona + abierta)



# ** Estas funciones no están en uso, en pruebas. Comienza en línea 46**

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

# ** Comienza aquí **

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

def _CCV(letra, letra_siguiente, letra_consiguiente):
    return es_consonante(letra) and es_inseparable(letra, letra_siguiente) and es_vocal(letra_consiguiente)   # V-(C)CV, C-(C)CV

def _CV(letra_anterior, letra, letra_siguiente):
    return es_consonante(letra) and not es_inseparable(letra_anterior, letra) and es_vocal(letra_siguiente)   # V-(C)V, C-(C)V

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

            if es_diptongo(letra_anterior, letra):                                       # Diptongo VV
                silaba=silaba+letra
            else:
                silabeo.append(silaba)
                silaba = letra

        elif es_consonante(letra):                                        #Estructuras C(C)V, C(C)C, V(C)V, V(C)C

            if _CCV(letra, letra_siguiente, letra_consiguiente) or _CV(letra_anterior, letra, letra_siguiente):        
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
