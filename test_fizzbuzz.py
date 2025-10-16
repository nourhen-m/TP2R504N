import unittest
import sys
from io import StringIO
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_commence_par_12(self):
        sortie = StringIO()
        sys.stdout = sortie

        affiche()


        resultat = sortie.getvalue().strip()
        self.assertTrue(resultat.startswith("12"), "La sortie doit commencer par '12'")

if __name__ == "__main__":
    unittest.main()
