import unittest
from cryptage import crypt

class TestCryptage(unittest.TestCase):
    def test_existence_et_type(self):
        res = crypt("")
        self.assertIsInstance(res, str, "crypt() doit retourner une chaîne")

if __name__ == "__main__":
    unittest.main()
