# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Syllabicate word according to rules of given language."""


from es import find_coda


def _get_new_word(word, i):
    newword = word[i:]
    return newword


def _add_letter(syllable, letter):
    return syllable + letter


def _get_syllable(word):
    syllable = ''
    for i, letter in enumerate(word):
        coda = find_coda(word, i)
        if coda is None:
            syllable += letter
            continue
        syllable = _add_letter(syllable, word[i:coda])
        return syllable
    return syllable


def syllabicate(word):
    """Return a list of syllables from word. Word data type must be unicode."""
    syllabification = []
    while len(word) > 0:
        syllable = _get_syllable(word)
        syllabification.append(syllable)
        word = _get_new_word(word, len(syllable))
    return syllabification
