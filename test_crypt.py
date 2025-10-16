import unittest
from crypt import crypt

class TestCryptage(unittest.TestCase):
    def test_existence_et_type(self):
        self.assertIsInstance(crypt(""), str)

    def test_a_devient_b(self):
        self.assertEqual(crypt("a"), "b")

    def test_crypt_accepte_un_pas(self):
        try:
            resultat = crypt("a", 2)
        except TypeError:
            self.fail("crypt() doit accepter 2 arguments (message, pas)")


if __name__ == "__main__":
    unittest.main()
