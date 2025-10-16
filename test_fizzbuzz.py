import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_affiche_quelque_chose(self):
        import io
        from contextlib import redirect_stdout
        from fizzbuzz import affiche

        buff = io.StringIO()
        with redirect_stdout(buff):
            affiche()
        out = buff.getvalue().strip()
	self.assertTrue(out.startswith("12"), "Début attendu '12'")



if __name__ == "__main__":
    unittest.main()
