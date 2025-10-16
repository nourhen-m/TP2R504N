import unittest
from fizzbuzz import affiche

class TestFizzBuzzPartieB(unittest.TestCase):
    def test_affiche_accepte_un_parametre(self):
        resultat = affiche(1)
        self.assertIsInstance(resultat, str, "affiche(n) doit retourner une chaîne")

    def test_affiche_1(self):
        self.assertEqual(affiche(1), "1")



if __name__ == "__main__":
    unittest.main()
