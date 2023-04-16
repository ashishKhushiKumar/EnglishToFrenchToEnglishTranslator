import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        print("englishToFrench: assertEqual : Passed")
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        print("englishToFrench: assertNotEqual : Passed")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        print("frenchToEnglish: assertEqual : Passed")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        print("frenchToEnglish: assertNotEqual : Passed")
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()
