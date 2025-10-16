import unittest
from decrypt import decrypt

class TestDecryptage(unittest.TestCase):
    def test_existence_et_type(self):
        res = decrypt("")
        self.assertIsInstance(res, str, "decrypt() doit retourner une chaîne")

    def test_inverse_simple(self):
        from crypt import crypt
        message = "abc"
        crypte = crypt(message)
        decrypte = decrypt(crypte)
        self.assertEqual(decrypte, message)

if __name__ == "__main__":
    unittest.main()
