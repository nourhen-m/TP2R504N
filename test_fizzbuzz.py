import unittest
from fizzbuzz import affiche

class TestFizzBuzzPartieB(unittest.TestCase):
    def test_affiche_accepte_un_parametre(self):
        self.assertIsInstance(affiche(5, 10), str)

    def test_affiche_5_a_10(self):
        self.assertEqual(affiche(5, 10), "BuzzFizz78FizzBuzz")

    def test_affiche_10_a_16(self):
        attendu = "Buzz11Fizz1314FrisBee16"
        self.assertEqual(affiche(10, 16), attendu)


if __name__ == "__main__":
    unittest.main()
