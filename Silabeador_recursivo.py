# encoding=Utf-8
# La funcionalidad está creada para la división silábica normativa de unidades discretas del español (palabras y pseudopalabras). No es aplicable a otras lenguas, a la transcripción fonética ni al análisis métrico del verso, pero se ha intentado crear una estructura flexible, que permita la reutilización y adaptación del código a otras lenguas y reglas.

# Se aplican las reglas de división silábica expuestas en Quilis, Tratado de fonética y fonología, p. 368 y ss.
#   V=vocal C = consonante.

#   1. VCV =      V-CV 'a-mo'

#   2. VCCV =     a) VC-CV 'ar-mo'
#                 b) V-CCV 'a-bro' [(b, c, f, g, k, p) + (l, r), dr, tr, ch, ll, rr]

#   3. VCCC(C)V = a)VCC (ns, bs) - (C)CV 'ins-tante', 'obs- truir'
#                 b)VC-CCV 'in-tra' (grupo inseparable)

#   4. VV =       a) V-V 've-a', 'le-í-a' (abiertas, abierta + cerrada tónica, cerrada tónica + abierta)
#                 b) VV 'au-ra' (cerradas, abierta+cerrada átona, cerrada átona + abierta)


# La consonante se define por no poder ser núcleo silábico ni constituir sílaba por sí misma. Las semivocales 'y, w' y la letra hache son tratadas siempre como consonantes, por lo que algunas palabras, especialmente los extranjerismos, reciben una segmentación incorrecta , 'billy', mientras otros casos se acercan a la división hecha por un hispanohablante que desconociera la fonética del idioma original: 've-ge-ta-ble', 'a-mat-xu'

# Algunos prefijos ('sub', 'psi' o 'pso') producen errores 'su-bín-dice*' por 'sub-ín-di-ce', 'pa-rap-si-có-lo-go*' por 'pa-ra-psi-có-lo-go', etc., estos elementos no siguen la regla general de agrupamiento al percibirse como unidad con significado independiente cuya identidad de sentido se prioriza sobre el uso fonético, si bien existen casos límite donde el prefijo está prácticamente lexicalizado 'su-bra-yar / sub-ra-yar'. Esto no ocurre con otras palabras o pseudopalabras donde, por no apreciarse unidad semántica, el hispanohablante se rige por la norma y agrupa la consonante con la vocal que le sigue: 'rap-so-da', 'pep-si', 'su-bli-me'.

def _get_encoding():
    encoding = 'utf-8'
    return encoding


def _decode_str(text):
    if type(text) is str:
        text = text.decode(_get_encoding())
    return text


def _spa():
    consonants = map(lambda word: unicode(word, 'utf-8'), ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    vowels = map(lambda word: unicode(word, 'utf-8'), ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü'])
    indivisibleConsonants = map(lambda word: unicode(word, 'utf-8'), ['ch', 'll', 'rr', 'pr', 'pl', 'br', 'bl', 'fr', 'fl', 'gr', 'gl', 'kr', 'cr', 'kl', 'cl', 'dr', 'tr'])
    closedVowels = map(lambda text: unicode(text, 'utf-8'), ['i', 'u', 'ü'])
    alphabet = [consonants, vowels, indivisibleConsonants, closedVowels]
    return alphabet


def _getConsonants(language):
    consonants = language[0]
    return consonants


def _getVowels(language):
    vowels = language[1]
    return vowels


def _getIndivisibleConsonants(language):
    indivisibleConsonants = language[2]
    return indivisibleConsonants


def _getClosedVowels(language):
    closedVowels = language[3]
    return closedVowels


def _isVowel(letter):
    vowels = _getVowels(_spa())
    return letter in vowels


def _isConsonant(letter):
    consonants = _getConsonants(_spa())
    return letter in consonants


def _isIndivisible(letter):
    consonants = _getIndivisibleConsonants(_spa())
    return letter in consonants

def _VV(text, i):
    if len(text[i:]) >= 2:
        return _isVowel(text[i]) and _isVowel(text[i+1])


def _Diphthong(text, i):
    closedVowels = _getClosedVowels(_spa())
    if len(text) >= 2 and _VV(text, i):
        return text[i] in closedVowels or text[i+1] in closedVowels


def _Hiatus(text, i):
    if len(text) >= 2:
        return _VV(text, i) and not _Diphthong(text, i)


def _CV(text):
    if len(text) >= 2:
        return _isConsonant(text[0]) and _isVowel(text[1])


def _V_CV(text, i):
    if len(text[i:]) >= 3:
        return _isVowel(text[i]) and _isConsonant(text[i+1]) and _isVowel(text[i+2])


def _V_CCV(text, i):
    if len(text[i:]) >= 4:
        return _isVowel(text[i]) and _isIndivisible(text[i+1:i+3]) and _isVowel(text[i+3])


def _VC_CV(text, i):
    if len(text[i:]) >= 4:
        return _isVowel(text[i]) and _isConsonant(text[i+1]) and _isConsonant(text[i+2]) and _isVowel(text[i+3]) and not _isIndivisible(text[i+1:i+3])


def _VC_CCV(text, i):
    if len(text[i:]) >= 5:
        return _isVowel(text[i]) and _isConsonant(text[i+1]) and _isIndivisible(text[i+2:i+4]) and _isVowel(text[i+4])


def _VCC_CV(text, i):
    if len(text[i:]) >= 5:
        return _isVowel(text[i]) and _isConsonant(text[i+1]) and _isConsonant(text[i+2]) and _isConsonant(text[i+3]) and _isVowel(text[i+4]) and not _isIndivisible(text[i+2:i+4])


def _VCC_CCV(text, i):
    if len(text[i:]) >= 6:
        return _isVowel(text[i]) and _isConsonant(text[i+1]) and _isConsonant(text[i+2]) and _isIndivisible(text[i+3:i+5]) and _isVowel(text[i+5])


def _getNewText(text, i):
    newText = text[i:]
    return newText


def _addLetter(syllable, letter):
    return syllable + letter


def _findSyllable(text, syllable):
    i = 0
    if _isConsonant(text[i]) or _Diphthong(text, i):
        syllable = _addLetter(syllable, text[i])
        return _findSyllable(_getNewText(text, i+1), syllable)
    if _V_CCV(text, i) or _V_CV(text, i) or _Hiatus(text, i):
        syllable = _addLetter(syllable, text[i])
        return syllable
    if _VC_CV(text, i) or _VC_CCV(text, i):
        syllable = _addLetter(syllable, text[i:i+2])
        return syllable
    if _VCC_CV(text, i) or _VCC_CCV(text, i):
        syllable = _addLetter(syllable, text[i:i+3])
        return syllable
    else:
        syllable = _addLetter(syllable, text[:])
        return syllable


def _Syllabification(text, syllabification):
    if len(text) > 0:
        syllable = _findSyllable(text, '')
        syllabification.append(syllable)
        newText = _getNewText(text, len(syllable))
        return _Syllabification(newText, syllabification)
    return syllabification


def syllabicate(text):
    """Syllabicate text given according to language rules."""
    text = _decode_str(text)
    syllabification = _Syllabification(text, [])
    syllabification = [i.encode(_get_encoding())for i in syllabification]
    return syllabification


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
