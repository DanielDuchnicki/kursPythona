import unittest
from spotkanie1.zadanie7 import klasyfikator
from spotkanie1.zadanie7 import NotStringError


class TestKlasyfikator(unittest.TestCase):

    def test_kontrolaargumentu(self):
        with self.assertRaises(NotStringError):
            klasyfikator(123)


if __name__ == '__main__':
    unittest.main()
