import unittest
from fizzbuzz import affiche

class TestFizzBuzzPartieB(unittest.TestCase):
    def test_affiche_accepte_un_parametre(self):
        resultat = affiche(1)
        self.assertIsInstance(resultat, str)

    def test_affiche_1(self):
        self.assertEqual(affiche(1), "1")

    def test_affiche_2(self):
        self.assertEqual(affiche(2), "12")
    def test_fizz_pour_3(self):
        self.assertEqual(affiche(3), "12Fizz")

if __name__ == "__main__":
    unittest.main()
