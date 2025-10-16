import unittest
from crypt import crypt

class TestCryptage(unittest.TestCase):
    def test_existence_et_type(self):
        self.assertIsInstance(crypt(""), str)

    def test_a_devient_b(self):
        self.assertEqual(crypt("a"), "b")
if __name__ == "__main__":
    unittest.main()
