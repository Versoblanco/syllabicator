# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test syllabicator."""

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

import unittest
import syllabicator
import stress
import es as lang


class _Testsyllabicator(unittest.TestCase):

    def test_syllabicate_semivowel(self):
        words = ['pytyngoyaxtllynstymal']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['py', 'tyn', 'go', 'yaxt', 'llyns', 'ty', 'mal']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_xenism(self):
        words = ['whiskey', 'amatxu']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['whis', 'key'], ['a', 'ma', 'txu']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_consonant_vowel(self):
        words = ['pepero']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['pe', 'pe', 'ro']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_diptongo(self):
        words = ['luisnau', u'cigüeña']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['luis', 'nau'], ['ci', u'güe', u'ña']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_hiato(self):
        words = ['peana', 'continuum']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['pe', 'a', 'na'], ['con', 'ti', 'nu', 'um']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_hiato_con_tilde(self):
        words = [u'leía']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['le', u'í', 'a']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_triptongo(self):
        words = ['miauriui']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['miau', 'riui']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_two_consonants_inseparables_between_two_voweles(self):
        words = ['itralla']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['i', 'tra', 'lla']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_two_consonants_between_two_vowels(self):
        words = ['insa']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['in', 'sa']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_three_consonants_with_inseparable_group_between_two_voweles(self):
        words = ['intra']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['in', 'tra']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_three_consonants_between_two_vowels(self):
        words = ['insta', 'ashlo']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['ins', 'ta'], ['ash', 'lo']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_four_consonants_between_two_voweles(self):
        words = ['instra']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['ins', 'tra']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_prefix(self):  # Check wrong syllabification (no prefix functionality)
        words = [u'subacuático', u'parapsicólogo', 'postimpresionismo', 'subrepticio']
        words = [syllabicator.syllabicate(word, lang) for word in words]
        syllabification = [['su', 'ba', u'cuá', 'ti', 'co'],
                           ['pa', 'rap', 'si', u'có', 'lo', 'go'],
                           ['pos', 'tim', 'pre', 'sio', 'nis', 'mo'],
                           ['su', 'brep', 'ti', 'cio']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_tonic(self):  # Check tonic syllables
        words = [u'tú', 'tecla', 'latir', u'árbol', u'afín', u'esdrújula', u'rápidamente']
        words = [stress.tonic(word, lang) for word in words]
        stressed = [u'tú', 'te', 'tir', u'ár', u'fín', u'drú', u'rá']
        self.assertSequenceEqual(stressed, words)

    def test_syllabicate_atonic(self):  # Check atonic syllables
        words = [u'tú', 'tecla', 'latir', u'árbol', u'afín', u'esdrújula',
                 u'rápidamente']
        words = [stress.atonic(word, lang) for word in words]
        unstressed = [[], ['cla'], ['la'], ['bol'], ['a'], ['es', 'ju', 'la'],
                      ['pi', 'da', 'men', 'te']]
        self.assertSequenceEqual(unstressed, words)


if __name__ == '__main__':
    unittest.main()
