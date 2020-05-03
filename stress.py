# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find stressed syllable according to rules of given language."""

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

import syllabicator
import es as lang

def get_tonic(syllables, lang):
    """Return tonic syllable from a list of syllables."""
    return syllables[lang.find_stress(syllables)]

def tonic(word, lang):    
    """Return tonic syllable from a word."""
    syllables = syllabicator.syllabicate(word, lang)
    return get_tonic(syllables, lang)

def atonic(word, lang):
    """Return atonic syllable/s from a word."""
    return 0
