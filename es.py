# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Spanish alphabet and syllabification rules."""

# TODO: new class language?. Atributtes: alphabet, patterns, boundaries


def _alphabet():
    consonants = map(lambda word: unicode(word, 'utf-8'), ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    vowels = map(lambda word: unicode(word, 'utf-8'), ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü'])
    semivowels = map(lambda word: unicode(word, 'utf-8'), ['y'])
    indivisibleConsonants = map(lambda word: unicode(word, 'utf-8'), ['ch', 'll', 'rr', 'pr', 'pl', 'br', 'bl', 'fr', 'fl', 'gr', 'gl', 'kr', 'cr', 'kl', 'cl', 'dr', 'tr', 'tx'])
    closedVowels = map(lambda text: unicode(text, 'utf-8'), ['i', 'u', 'ü'])
    alphabet = {'consonants': consonants, 'vowels': vowels, 'semivowels': semivowels,  'indivisibleConsonants': indivisibleConsonants, 'closedVowels': closedVowels}
    return alphabet


def _closed_vowels():
    return _alphabet()['closedVowels']


def _is_vowel(letter):
    return letter in _alphabet()['vowels']


def _is_semivowel(letter):
    return letter in _alphabet()['semivowels']


def _is_vowel_OR_semivowel(letter):
    return _is_vowel(letter) or _is_semivowel(letter)


def _is_consonant(letter):
    return letter in _alphabet()['consonants']


def _is_indivisible(letter):
    return letter in _alphabet()['indivisibleConsonants']


# V 'vowel' C 'consonant'


def _VV(text, i):
    if len(text[i:]) >= 2:
        return _is_vowel(text[i]) and _is_vowel(text[i+1])


def _Diphthong(text, i):
    if len(text) >= 2 and _VV(text, i):
        return text[i] in _closed_vowels() or text[i+1] in _closed_vowels()


def _Hiatus(text, i):
    if len(text) >= 2:
        return _VV(text, i) and not _Diphthong(text, i)


def _CV(text):
    if len(text) >= 2:
        return _is_consonant(text[0]) and _is_vowel(text[1])


def _V_CV(text, i):
    if len(text[i:]) >= 3:
        return _is_vowel_OR_semivowel(text[i]) and _is_consonant(text[i+1]) and _is_vowel_OR_semivowel(text[i+2])


def _V_CCV(text, i):
    if len(text[i:]) >= 4:
        return _is_vowel_OR_semivowel(text[i]) and _is_indivisible(text[i+1:i+3]) and _is_vowel_OR_semivowel(text[i+3])


def _VC_CV(text, i):
    if len(text[i:]) >= 4:
        return _is_vowel_OR_semivowel(text[i]) and _is_consonant(text[i+1]) and _is_consonant(text[i+2]) and _is_vowel_OR_semivowel(text[i+3]) and not _is_indivisible(text[i+1:i+3])


def _VC_CCV(text, i):
    if len(text[i:]) >= 5:
        return _is_vowel_OR_semivowel(text[i]) and _is_consonant(text[i+1]) and _is_indivisible(text[i+2:i+4]) and _is_vowel_OR_semivowel(text[i+4])


def _VCC_CV(text, i):
    if len(text[i:]) >= 5:
        return _is_vowel_OR_semivowel(text[i]) and _is_consonant(text[i+1]) and _is_consonant(text[i+2]) and _is_consonant(text[i+3]) and _is_vowel_OR_semivowel(text[i+4]) and not _is_indivisible(text[i+2:i+4])


def _VCC_CCV(text, i):
    if len(text[i:]) >= 6:
        return _is_vowel_OR_semivowel(text[i]) and _is_consonant(text[i+1]) and _is_consonant(text[i+2]) and _is_indivisible(text[i+3:i+5]) and _is_vowel_OR_semivowel(text[i+5])


def get_pattern(text, i):
    """Find pattern and return its name."""
    # TODO: Refactor to iterable
    if _V_CCV(text, i):
        return 'V_CCV'
    if _V_CV(text, i):
        return 'V_CV'
    if _Hiatus(text, i):
        return 'Hiatus'
    if _VC_CV(text, i):
        return 'VC_CV'
    if _VC_CCV(text, i):
        return 'VC_CCV'
    if _VCC_CV(text, i):
        return 'VCC_CV'
    if _VCC_CCV(text, i):
        return 'VCC_CCV'
    else:
        return None


def boundary(pattern, i):
    """Return syllable boundary endpoint for given pattern."""
    # TODO: Generalise and move to main program. Relocate boundaries dict
    boundaries = {'V_CCV': 1, 'V_CV': 1, 'Hiatus': 1, 'VC_CV': 2, 'VC_CCV': 2, 'VCC_CV': 3, 'VCC_CCV': 3}
    return i + boundaries[pattern]
