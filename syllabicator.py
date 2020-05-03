# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Syllabicate word according to rules of given language."""

# Copyright 2019 Patricia Martín (aka Farándula)

# This file is part of syllabicator.
# Syllabicator is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your option)
# any later version.
# Syllabicator is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with Syllabicator. If not, see <https://www.gnu.org/licenses/>.


def _get_syllable(word, lang):
    lenght = lang.len_syllable(word)
    syllable = word[:lenght]
    return syllable


def syllabicate(word, lang):
    """Return a list of syllables from word. Word data type must be unicode."""
    syllabification = []
    while len(word) > 0:
        syllable = _get_syllable(word, lang)
        syllabification.append(syllable)
        word = word[len(syllable):]
    return syllabification
