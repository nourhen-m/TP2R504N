import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_retourne_du_texte(self):
        resultat = affiche()
        self.assertIsInstance(resultat, str, "affiche() doit retourner une chaîne de caractères")

if __name__ == "__main__":
    unittest.main()
