# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test Silabeador."""

import unittest
import Silabeador


class _TestSilabeador(unittest.TestCase):

    def test_syllabicate_semivowel(self):
        words = ['pytyngoyaxtllynstymal']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['py', 'tyn', 'go', 'yaxt', 'llyns', 'ty', 'mal']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_xenism(self):
        words = ['whiskey', 'amatxu']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['whis', 'key'], ['a', 'ma', 'txu']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_consonant_vowel(self):
        words = ['pepero']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['pe', 'pe', 'ro']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_diptongo(self):
        words = ['luisnau', u'cigüeña']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['luis', 'nau'], ['ci', u'güe', u'ña']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_hiato(self):
        words = ['peana', 'continuum']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['pe', 'a', 'na'], ['con', 'ti', 'nu', 'um']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_hiato_con_tilde(self):
        words = [u'leía']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['le', u'í', 'a']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_triptongo(self):
        words = ['miauriui']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['miau', 'riui']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_two_consonants_inseparables_between_two_voweles(self):
        words = ['itralla']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['i', 'tra', 'lla']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_two_consonants_between_two_vowels(self):
        words = ['insa']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['in', 'sa']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_three_consonants_with_inseparable_group_between_two_voweles(self):
        words = ['intra']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['in', 'tra']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_three_consonants_between_two_vowels(self):
        words = ['insta', 'ashlo']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['ins', 'ta'], ['ash', 'lo']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_cuatro_consonants_between_two_voweles(self):
        words = ['instra']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['ins', 'tra']]
        self.assertSequenceEqual(syllabification, words)

    def test_syllabicate_prefix(self):  # Check wrong syllabification (no prefix functionality)
        words = [u'subacuático', u'parapsicólogo', 'postimpresionismo', 'subrepticio']
        words = [Silabeador.syllabicate(word) for word in words]
        syllabification = [['su', 'ba', u'cuá', 'ti', 'co'], ['pa', 'rap', 'si', u'có', 'lo', 'go'], ['pos', 'tim', 'pre', 'sio', 'nis', 'mo'], ['su', 'brep', 'ti', 'cio']]
        self.assertSequenceEqual(syllabification, words)


if __name__ == '__main__':
    unittest.main()
