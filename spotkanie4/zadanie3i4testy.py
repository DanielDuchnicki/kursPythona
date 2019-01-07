import unittest
from spotkanie4.zadanie3i4 import *


class TestKlasyfikator(unittest.TestCase):

    def test_Zmienna(self):
        with self.assertRaises(NotStringError):
            Zmienna(123)

    def test_Stala(self):
        with self.assertRaises(NotIntError):
            Stala("abcd")

    def test_Dodawanie(self):
        aktualny_stan = {'x': 1, 'y': 3, 'z': 3}
        wyrazenie = Dodawanie(Zmienna("x"), Zmienna("y"))
        self.assertEqual(wyrazenie.oblicz(aktualny_stan), 4)

    def test_Mnozenie(self):
        aktualny_stan = {'x': 1, 'y': 3, 'z': 3}
        wyrazenie = Mnozenie(Zmienna("x"), Zmienna("y"))
        self.assertEqual(wyrazenie.oblicz(aktualny_stan), 3)


if __name__ == '__main__':
    unittest.main()
