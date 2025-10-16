import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_existe(self):
        try:
            affiche()
        except NameError:
            self.fail("La fonction affiche() doit exister")

if __name__ == "__main__":
    unittest.main()
