# encoding=Utf-8


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
    semivowels = map(lambda word: unicode(word, 'utf-8'), ['y'])
    indivisibleConsonants = map(lambda word: unicode(word, 'utf-8'), ['ch', 'll', 'rr', 'pr', 'pl', 'br', 'bl', 'fr', 'fl', 'gr', 'gl', 'kr', 'cr', 'kl', 'cl', 'dr', 'tr'])
    closedVowels = map(lambda text: unicode(text, 'utf-8'), ['i', 'u', 'ü'])
    alphabet = [consonants, vowels, semivowels,  indivisibleConsonants, closedVowels]
    return alphabet


def _consonants(language):
    consonants = language[0]
    return consonants


def _vowels(language):
    vowels = language[1]
    return vowels


def _semivowels(language):
    semivowels = language[2]
    return semivowels


def _indivisibleConsonants(language):
    indivisibleConsonants = language[3]
    return indivisibleConsonants


def _closedVowels(language):
    closedVowels = language[4]
    return closedVowels


def _isVowel(letter):
    return letter in _vowels(_spa())


def _isSemivowel(letter):
    return letter in _semivowels(_spa())


def _isVowelORSemivowel(letter):
    return _isVowel(letter) or _isSemivowel(letter)


def _isConsonant(letter):
    return letter in _consonants(_spa())


def _isIndivisible(letter):
    return letter in _indivisibleConsonants(_spa())

# V= vowel C = consonant


def _VV(text, i):
    if len(text[i:]) >= 2:
        return _isVowel(text[i]) and _isVowel(text[i+1])


def _Diphthong(text, i):
    if len(text) >= 2 and _VV(text, i):
        return text[i] in _closedVowels(_spa()) or text[i+1] in _closedVowels(_spa())


def _Hiatus(text, i):
    if len(text) >= 2:
        return _VV(text, i) and not _Diphthong(text, i)


def _CV(text):
    if len(text) >= 2:
        return _isConsonant(text[0]) and _isVowel(text[1])


def _V_CV(text, i):
    if len(text[i:]) >= 3:
        return _isVowelORSemivowel(text[i]) and _isConsonant(text[i+1]) and _isVowelORSemivowel(text[i+2])


def _V_CCV(text, i):
    if len(text[i:]) >= 4:
        return _isVowelORSemivowel(text[i]) and _isIndivisible(text[i+1:i+3]) and _isVowelORSemivowel(text[i+3])


def _VC_CV(text, i):
    if len(text[i:]) >= 4:
        return _isVowelORSemivowel(text[i]) and _isConsonant(text[i+1]) and _isConsonant(text[i+2]) and _isVowelORSemivowel(text[i+3]) and not _isIndivisible(text[i+1:i+3])


def _VC_CCV(text, i):
    if len(text[i:]) >= 5:
        return _isVowelORSemivowel(text[i]) and _isConsonant(text[i+1]) and _isIndivisible(text[i+2:i+4]) and _isVowelORSemivowel(text[i+4])


def _VCC_CV(text, i):
    if len(text[i:]) >= 5:
        return _isVowelORSemivowel(text[i]) and _isConsonant(text[i+1]) and _isConsonant(text[i+2]) and _isConsonant(text[i+3]) and _isVowelORSemivowel(text[i+4]) and not _isIndivisible(text[i+2:i+4])


def _VCC_CCV(text, i):
    if len(text[i:]) >= 6:
        return _isVowelORSemivowel(text[i]) and _isConsonant(text[i+1]) and _isConsonant(text[i+2]) and _isIndivisible(text[i+3:i+5]) and _isVowelORSemivowel(text[i+5])


def _getNewText(text, i):
    newText = text[i:]
    return newText


def _addLetter(syllable, letter):
    return syllable + letter


def _findVowelORSemivowel(text):
    def nextLetter(text, i):
        if len(text) > i+1:
            return text[i+1]

    for i, letter in enumerate(text):
        vowelIndex = i
        if _Hiatus(text, i):
            break
        if _isVowelORSemivowel(letter) and _isConsonant(nextLetter(text, i)):
            break
    print vowelIndex
    return vowelIndex


def _findSyllable(text):
    i = _findVowelORSemivowel(text)
    syllable = text[:i]
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
        syllable = _addLetter(syllable, text[i:])
        return syllable


def _Syllabification(text, syllabification):
    if len(text) > 0:
        syllable = _findSyllable(text)
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


def _askText():
    while True:
        text = raw_input('Escriba la palabra (exit para salir): ')
        if text == 'exit':
            exit()
        if len(text) > 0:
            return text


def _formatText(text):
    text = text.strip().lower()
    text = ''.join(text)
    return text
