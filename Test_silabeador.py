#coding=UTF-8

import unittest
import Silabeador

class TestSilabeador(unittest.TestCase):

    def test_silabear_consonante_vocal(self):
        palabra = 'pepe'
        self.assertEqual(['pe', 'pe'], Silabeador.silabear(palabra))

    def test_silabear_diptongo(self):
        palabra = 'sauna'
        self.assertEqual(['sau', 'na'], Silabeador.silabear(palabra))

    def test_silabear_hiato(self):
        palabra = 'peana'
        self.assertEqual(['pe', 'a', 'na'], Silabeador.silabear(palabra))

    def test_silabear_hiato_con_tilde(self):
        palabra = 'leía'
        self.assertEqual(['le', u'í', 'a'], Silabeador.silabear(palabra))

    def test_silabear_triptongo(self):
        palabra = 'miau'
        self.assertEqual(['miau'], Silabeador.silabear(palabra))

    def test_silabear_dos_consonantes_inseparables_entre_dos_vocales(self):
        palabra = 'itra'
        self.assertEqual(['i', 'tra'], Silabeador.silabear(palabra))

    def test_silabear_dos_consonantes_entre_dos_vocales(self):
        palabra = 'insa'
        self.assertEqual(['in', 'sa'], Silabeador.silabear(palabra))

    def test_silabear_tres_consonantes__con_grupo_inseparable_entre_dos_vocales(self):
        palabra = 'intra'
        self.assertEqual(['in', 'tra'], Silabeador.silabear(palabra))

    def test_silabear_tres_consonantes_entre_dos_vocales(self):
        palabra = 'insta'
        self.assertEqual(['ins', 'ta'], Silabeador.silabear(palabra))

    def test_silabear_cuatro_consonantes_entre_dos_vocales(self):
        palabra = 'instra'
        self.assertEqual(['ins', 'tra'], Silabeador.silabear(palabra))

if __name__ == '__main__':
    unittest.main()

# Problemas con la codificación en palabras con tilde, el input debe ser utf-8
#test_palabras=[cigüeña, , , día, guerrero, pingüino, guirigai, caray, yerro, hierro, yermo, bíceps, psicólogo, aceptar, subrogar, subrepticio]
#test_correcto=[]
