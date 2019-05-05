#coding=UTF-8

# La funcionalidad está creada para la división silábica normativa de unidades discretas del español (palabras y pseudopalabras). No es aplicable a otra lenguas, a la transcripción fonética ni al análisis métrico del verso, aunque podría adaptarse para los dos últimos casos con relativa facilidad.

# Se aplican las reglas de división silábica expuestas en Quilis, Tratado de fonética y fonología, p. 368 y ss.
#   V=vocal C = consonante.

#   1. VCV =      V-CV 'a-mo'

#   2. VCCV =     a) VC-CV 'ar-mo'
#                 b) V-CCV 'a-bro' [(b, c, f, g, k, p) + (l, r), dr, tr, ch, ll, rr]

#   3. VCCC(C)V = a)VCC (ns, bs) - (C)CV 'ins-tante', 'obs- truir'
#                 b)VC-CCV 'in-tra' (grupo inseparable)

#   4. VV =       a) V-V 've-a', 'le-í-a' (abiertas, abierta + cerrada tónica, cerrada tónica + abierta)
#                 b) VV 'au-ra' (cerradas, abierta+cerrada átona, cerrada átona + abierta)


# La consonante se define por no poder ser núcleo silábico ni constituir sílaba por sí misma. Las semivocales 'y, w' y la letra hache son tratadas siempre como consonantes, por lo que algunas palabras, especialmente los extranjerismos, reciben una segmentación incorrecta 'w-his-key', 'billy', mientras otros casos se acercan a la división hecha por un hispanohablante que desconociera la fonética del idioma original 's-pain', 've-ge-ta-ble', 'a-mat-xu'

# Algunos prefijos ('sub', 'psi' o 'pso') producen errores 'su-bín-dice*', 'pa-rap-si-có-lo-go*', 'p-so-ria-sis*', estos elementos no siguen la regla general de agrupamiento al percibirse como unidad con significado independiente cuya identidad de sentido se prioriza sobre el uso fonético, si bien existen casos límite donde el prefijo está prácticamente lexicalizado 'su-bra-yar / sub-ra-yar'. Esto no ocurre con otras palabras o pseudopalabras donde, por no apreciarse unidad semántica, el hispanohablante se rige por la norma y agrupa la consonante con la vocal que le sigue: 'rap-so-da', 'pep-si', 'su-bli-me'.

def definir_consonantes():
    consonantes = map(lambda word: unicode(word, 'utf-8'),
                      ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    return consonantes

def definir_vocales():
    vocales = map(lambda word: unicode(word, 'utf-8'), ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü'])
    return vocales

def definir_inseparables():
    inseparables = map(lambda word: unicode(word, 'utf-8'), ['ch', 'll', 'rr', 'pr', 'pl', 'br', 'bl', 'fr', 'fl', 'gr', 'gl', 'kr', 'cr', 'kl', 'cl', 'dr', 'tr'])
    return inseparables

def es_vocal(letra):
    vocales = definir_vocales()
    return letra in vocales

def es_consonante(letra):
    consonantes =  definir_consonantes()
    return letra in consonantes

def es_inseparable(letra1, letra2):
    inseparables = definir_inseparables()
    if not letra1 or not letra2:
        return False
    return letra1+letra2 in inseparables

def VV(letra_anterior, letra):
    return es_vocal(letra) and es_vocal(letra_anterior)

def es_diptongo(letra_anterior, letra):
    vcerradas = map(lambda word: unicode(word, 'utf-8'), ['i', 'u', 'ü'])
    return letra_anterior in vcerradas or letra in vcerradas

def es_hiato(letra_anterior, letra):
    return not es_diptongo(letra_anterior, letra)

def CV_(letra_anterior, letra):
    return es_vocal(letra) and es_consonante(letra_anterior)

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

def extraer_silaba(silabeo, silaba):
    silabeo.append(silaba)

def pedir_palabra():
    while True:
        palabra = raw_input('Escriba la palabra (exit para salir): ')
        if palabra == 'exit':
            exit()
        if len(palabra) > 0:
            return palabra

def dar_formato(palabra):
    palabra = palabra.strip().lower()
    palabra = ''.join(palabra)
    return palabra

def silabear(palabra):
    palabra = palabra.decode('utf-8')
    silaba = ''
    silabeo = []

    for index, letra in enumerate(palabra):

        letra_anterior = buscar_letra_anterior(palabra, index)
        letra_siguiente = buscar_letra_siguiente(palabra, index)
        letra_consiguiente = buscar_letra_consiguiente(palabra, index)

        if index==0:
            silaba=letra
            continue

        elif CV_(letra_anterior, letra):           # La vocal se agrupa siempre con la consonante anterior
            silaba=silaba+letra
            continue

        elif VV(letra_anterior, letra):

            if es_diptongo(letra_anterior, letra):
                silaba=silaba+letra
                continue
            elif es_hiato(letra_anterior, letra):
                extraer_silaba(silabeo, silaba)
                silaba = letra
                continue

        #Estructuras C(C)V, C(C)C, V(C)V, V(C)C

        elif _CCV(letra, letra_siguiente, letra_consiguiente) or _CV(letra_anterior, letra, letra_siguiente):
            extraer_silaba(silabeo, silaba)
            silaba = letra
            continue

        # Resto de consonantes
        elif es_consonante(letra):
            silaba=silaba+letra
            continue

        else:
            print 'Error'
            break

    extraer_silaba(silabeo, silaba)
    print silabeo
    return silabeo

def silabeador():
    while True:
        palabra = pedir_palabra()
        palabra = dar_formato(palabra)
        print 'Silabeo de ' + palabra
        silabeo = silabear(palabra)
        silabeo = '-'.join(silabeo)
        print silabeo
if __name__ == '__main__':
    silabeador()
