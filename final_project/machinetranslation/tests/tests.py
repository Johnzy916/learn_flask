import unittest

from translator import english_to_french,french_to_english

class TestE2F(unittest.TestCase):
    def test_null(self):
        self.assertIsNotNone(english_to_french('Hello'))

    def test_translate(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestF2E(unittest.TestCase):
    def test_null(self):
        self.assertIsNotNone(french_to_english('Bonjour'))

    def test_translate(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
