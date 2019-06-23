# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Syllabicate word according to rules of given language."""


def _get_syllable(word, lang):
    coda = lang.find_coda(word)
    syllable = word[:coda]
    return syllable


def syllabicate(word, lang):
    """Return a list of syllables from word. Word data type must be unicode."""
    syllabification = []
    while len(word) > 0:
        syllable = _get_syllable(word, lang)
        syllabification.append(syllable)
        word = word[len(syllable):]
    return syllabification
