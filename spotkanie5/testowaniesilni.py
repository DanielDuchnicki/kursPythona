import unittest
from spotkanie5.silnia import silnia
from spotkanie5.silnia import NotIntError


class TestSilnia(unittest.TestCase):

    def test_wyniku(self):
        self.assertEqual(silnia(0), 1)
        self.assertEqual(silnia(2), 2)
        self.assertEqual(silnia(3), 6)

    def test_kontrolaargumentu(self):
        with self.assertRaises(NotIntError):
            silnia("trzy")


if __name__ == '__main__':
    unittest.main()
