import unittest
import sys
from io import StringIO
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_commence_par_12_et_contient_Fizz(self):
        sortie = StringIO()
        sys.stdout = sortie
        affiche()
        resultat = sortie.getvalue().strip()

        self.assertTrue(resultat.startswith("12"), "Doit commencer par '12'")
        self.assertIn("Fizz", resultat, "3 doit être remplacé par Fizz")

if __name__ == "__main__":
    unittest.main()
