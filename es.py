# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Spanish alphabet and syllabification rules."""


def _alphabet():
    consonants = map(lambda word: unicode(word, 'utf-8'), ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    vowels = map(lambda word: unicode(word, 'utf-8'), ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'y'])
    indivisibleConsonants = map(lambda word: unicode(word, 'utf-8'), ['ch', 'll', 'rr', 'pr', 'pl', 'br', 'vr', 'bl', 'vl', 'fr', 'fl', 'gr', 'gl', 'kr', 'cr', 'kl', 'cl', 'dr', 'tr', 'tx'])
    closedVowels = map(lambda text: unicode(text, 'utf-8'), ['i', 'u', 'ü'])
    alphabet = {'consonants': consonants, 'vowels': vowels, 'indivisibleConsonants': indivisibleConsonants, 'closedVowels': closedVowels}
    return alphabet


def _closed_vowels():
    return _alphabet()['closedVowels']


def _is_vowel(letter):
    return letter in _alphabet()['vowels']


def _is_consonant(letter):
    return letter in _alphabet()['consonants']


def _is_indivisible(letter):
    return letter in _alphabet()['indivisibleConsonants']


# Patterns definitions. V = 'vowel' C = 'consonant'


def _VV(text, i):
    if len(text[i:]) >= 2:
        return not _is_consonant(text[i]) and not _is_consonant(text[i+1])


def _Diphthong(text, i):
    if len(text) >= 2:
        return text[i] in _closed_vowels() or text[i+1] in _closed_vowels()


def _V_V(text, i):
    if _VV(text, i):
        return not _Diphthong(text, i) or text[i] == text[i + 1]


def _CV(text):
    if len(text) >= 2:
        return _is_consonant(text[0]) and _is_vowel(text[1])


def _V_CV(text, i):
    if len(text[i:]) >= 3:
        return _is_vowel(text[i]) and _is_consonant(text[i+1]) and _is_vowel(text[i+2])


def _V_CCV(text, i):
    if len(text[i:]) >= 4:
        return _is_vowel(text[i]) and _is_indivisible(text[i+1:i+3]) and _is_vowel(text[i+3])


def _VC_CV(text, i):
    if len(text[i:]) >= 4:
        return _is_vowel(text[i]) and _is_consonant(text[i+1]) and _is_consonant(text[i+2]) and _is_vowel(text[i+3]) and not _is_indivisible(text[i+1:i+3])


def _VC_CCV(text, i):
    if len(text[i:]) >= 5:
        return _is_vowel(text[i]) and _is_consonant(text[i+1]) and _is_indivisible(text[i+2:i+4]) and _is_vowel(text[i+4])


def _VCC_CV(text, i):
    if len(text[i:]) >= 5:
        return _is_vowel(text[i]) and _is_consonant(text[i+1]) and _is_consonant(text[i+2]) and _is_consonant(text[i+3]) and _is_vowel(text[i+4]) and not _is_indivisible(text[i+2:i+4])


def _VCC_CCV(text, i):
    if len(text[i:]) >= 6:
        return _is_vowel(text[i]) and _is_consonant(text[i+1]) and _is_consonant(text[i+2]) and _is_indivisible(text[i+3:i+5]) and _is_vowel(text[i+5])


def get_pattern(text, i):
    """Find syllable's known pattern and return its name, otherwise return None."""
    patterns = {
      'V_CCV': _V_CCV(text, i),
      'V_CV': _V_CV(text, i),
      'V_V': _V_V(text, i), 'VC_CV': _VC_CV(text, i), 'VC_CCV': _VC_CCV(text, i), 'VCC_CV': _VCC_CV(text, i), 'VCC_CCV': _VCC_CCV(text, i)}
    for name in patterns:
        if patterns[name] is True:
            return name
        else:
            continue
    return None


def boundary(pattern, i):
    """Return number of letters until coda, including coda, for given pattern."""
    letters = {'V_CCV': 1, 'V_CV': 1, 'V_V': 1, 'VC_CV': 2, 'VC_CCV': 2, 'VCC_CV': 3, 'VCC_CCV': 3}
    return i + letters[pattern]
