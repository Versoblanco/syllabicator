# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Syllabicate text according to rules of given language."""

# TODO: Convert to Python3

from es import get_pattern, boundary
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
            b = boundary(pattern, i)
            syllable = _add_letter(syllable, text[i:b])
            return syllable
    return syllable


def _syllabification(text):
    syllabification = []
    while len(text) > 0:
        syllable = _get_syllable(text)
        syllabification.append(syllable)
        text = _get_new_text(text, len(syllable))
    return syllabification


def syllabicate(text):
    """Syllabicate this text according to this language rules."""
    text = decode_str(text)
    syllabification = _syllabification(text)
    syllabification = [i.encode(get_encoding())for i in syllabification]
    return syllabification
