# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Spanish alphabet and syllabification rules."""


def _alphabet():
    consonants = u'bcdfghjklmnñpqrstvwxyz'
    vowels = u'aeiouáéíóúüy'
    indivisibleConsonants = [u'ch', u'll', u'rr', u'pr', u'pl', u'br', u'vr', u'bl', u'vl', u'fr', u'fl', u'gr', u'gl', u'kr', u'cr', u'kl', u'cl', u'dr', u'tr', u'tx']
    closedVowels = u'iuü'
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


def _VV(word, i):
    if len(word[i:]) >= 2:
        return not _is_consonant(word[i]) and not _is_consonant(word[i+1])


def _Diphthong(word, i):
    if len(word) >= 2:
        return word[i] in _closed_vowels() or word[i+1] in _closed_vowels()


def _V_V(word, i):
    if _VV(word, i):
        return not _Diphthong(word, i) or word[i] == word[i + 1]


def _V_CV(word, i):
    if len(word[i:]) >= 3:
        return _is_vowel(word[i]) and _is_consonant(word[i+1]) and _is_vowel(word[i+2])


def _V_CCV(word, i):
    if len(word[i:]) >= 4:
        return _is_vowel(word[i]) and _is_indivisible(word[i+1:i+3]) and _is_vowel(word[i+3])


def _VC_CV(word, i):
    if len(word[i:]) >= 4:
        return _is_vowel(word[i]) and _is_consonant(word[i+1]) and _is_consonant(word[i+2]) and _is_vowel(word[i+3]) and not _is_indivisible(word[i+1:i+3])


def _VC_CCV(word, i):
    if len(word[i:]) >= 5:
        return _is_vowel(word[i]) and _is_consonant(word[i+1]) and _is_indivisible(word[i+2:i+4]) and _is_vowel(word[i+4])


def _VCC_CV(word, i):
    if len(word[i:]) >= 5:
        return _is_vowel(word[i]) and _is_consonant(word[i+1]) and _is_consonant(word[i+2]) and _is_consonant(word[i+3]) and _is_vowel(word[i+4]) and not _is_indivisible(word[i+2:i+4])


def _VCC_CCV(word, i):
    if len(word[i:]) >= 6:
        return _is_vowel(word[i]) and _is_consonant(word[i+1]) and _is_consonant(word[i+2]) and _is_indivisible(word[i+3:i+5]) and _is_vowel(word[i+5])


def find_coda(word):
    """Find last letter of first syllable (coda) and return next letter position."""
    coda = {
        _V_CCV: 1,
        _V_CV: 1,
        _V_V: 1,
        _VC_CV: 2,
        _VC_CCV: 2,
        _VCC_CV: 3,
        _VCC_CCV: 3,
    }
    for i, letter in enumerate(word):
        for pattern in coda:
            if pattern(word, i):
                return i + coda[pattern]
