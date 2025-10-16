import unittest
from fizzbuzz import affiche

class TestFizzBuzzPartieB(unittest.TestCase):
    def test_affiche_accepte_un_parametre(self):
        resultat = affiche(5, 10)
        self.assertIsInstance(resultat, str, "affiche(n1, n2) doit retourner une chaîne")



if __name__ == "__main__":
    unittest.main()
