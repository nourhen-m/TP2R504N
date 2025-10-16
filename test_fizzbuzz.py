import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_genere_1_a_5(self):
        resultat = affiche()
        attendu = "12Fizz4Buzz"
        self.assertEqual(resultat, attendu, "Le texte généré doit correspondre à 1→5")

if __name__ == "__main__":
    unittest.main()
