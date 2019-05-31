# -*- coding: utf-8 -*-

import unittest
import Silabeador_recursivo


class TestSilabeador_recursivo(unittest.TestCase):

    def test_syllabicate_semivowel(self):
        words = ['pytyngoyaxtllynstymal']
        syllabification = ['py', 'tyn', 'go', 'yaxt', 'llyns', 'ty', 'mal']
        for word in words:
            self.assertEqual(syllabification, Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_extranjerismos(self):
        words = ['whiskey']
        syllabification = ['whis', 'key']
        for word in words:
            self.assertEqual(syllabification, Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_extranjerismos(self):
        word = 'amatxu'
        self.assertEqual(['a', 'ma', 'txu'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_consonant_vowel(self):
        word = 'pepero'
        self.assertEqual(['pe', 'pe', 'ro'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_diptongo(self):
        word = 'luisnau'
        self.assertEqual(['luis', 'nau'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_hiato(self):
        word = 'peana'
        self.assertEqual(['pe', 'a', 'na'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_hiato_con_tilde(self):
        word = 'leía'
        self.assertEqual(['le', 'í', 'a'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_triptongo(self):
        word = 'miauriui'
        self.assertEqual(['miau', 'riui'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_two_consonants_inseparables_between_two_voweles(self):
        word = 'itralla'
        self.assertEqual(['i', 'tra', 'lla'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_two_consonants_between_two_vowels(self):
        word = 'insa'
        self.assertEqual(['in', 'sa'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_three_consonants_with_inseparable_group_between_two_voweles(self):
        word = 'intra'
        self.assertEqual(['in', 'tra'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_tres_consonants_between_two_voweles(self):
        word = 'insta'
        self.assertEqual(['ins', 'ta'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_cuatro_consonants_between_two_voweles(self):
        word = 'instra'
        self.assertEqual(['ins', 'tra'], Silabeador_recursivo.syllabicate(word))

    def test_syllabicate_ps_group(self):
        word = 'parapsicólogo'
        self.assertEqual(['pa', 'ra', 'psi', 'có', 'lo', 'go'], Silabeador_recursivo.syllabicate(word))


if __name__ == '__main__':
    unittest.main()


# Input must be utf-8
# test_words=[cigüeña, día, guerrero, pingüino, guirigai, caray, yerro, hierro, yermo, bíceps, psicólogo, aceptar, subrogar, subrepticio]
