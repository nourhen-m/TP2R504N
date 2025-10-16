import unittest
from decrypt import decrypt

class TestDecryptage(unittest.TestCase):
    def test_existence_et_type(self):
        res = decrypt("")
        self.assertIsInstance(res, str, "decrypt() doit retourner une chaîne")

if __name__ == "__main__":
    unittest.main()
