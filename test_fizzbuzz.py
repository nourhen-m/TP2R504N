import unittest
from fizzbuzz import affiche

class TestFizzBuzzPartieB(unittest.TestCase):
    def test_affiche_accepte_un_parametre(self):
        self.assertIsInstance(affiche(5, 10), str)

    def test_affiche_5_a_10(self):
        attendu = "BuzzFizz78FizzBuzz"
        self.assertEqual(affiche(5, 10), attendu)



if __name__ == "__main__":
    unittest.main()
