# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Syllabicate text according to rules of given language."""

# TODO: try with Python3

from es import get_pattern, coda
from encoding import get_encoding, decode_str


def _get_new_text(text, i):
    newText = text[i:]
    return newText


def _add_letter(syllable, letter):
    return syllable + letter


def _get_syllable(text):
    syllable = ''
    for i, letter in enumerate(text):
        pattern = get_pattern(text, i)
        if pattern is None:
            syllable = _add_letter(syllable, text[i])
            continue
        else:
            c = i + coda(pattern)
            syllable = _add_letter(syllable, text[i:c])
            return syllable
    return syllable


def _syllabification(text):
    """Return a list of syllables from text. Text data type must be unicode."""
    syllabification = []
    while len(text) > 0:
        syllable = _get_syllable(text)
        syllabification.append(syllable)
        text = _get_new_text(text, len(syllable))
    return syllabification


def syllabicate(text):
    """Get syllabification and return syllables as a list of byte strings. Text should be compound of correctly stressed spanish words or pseudowords, without spaces or non-spanish special chars. Data type must be bytes or unicode, with utf-8 compatible encoding (such as ASCII)."""
    text = decode_str(text)
    syllabification = _syllabification(text)
    syllabification = [i.encode(get_encoding())for i in syllabification]
    return syllabification
