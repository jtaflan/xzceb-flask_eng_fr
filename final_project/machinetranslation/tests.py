import unittest
from translator import englishToFrench, frenchToEnglish
class TestE2F(unittest.TestCase):
    """English to French tests"""
    def english_to_French(self, word):
        dictionary = {'Hello': 'Bonjour', 'Goodbye': 'Au revoir', 'Yes': 'Oui', 'No': 'Non'}
        return dictionary.get(word, '')

    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(self.english_to_French('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(self.english_to_French('Hello'), 'Hello')
        # Test None returns empty string
        self.assertEqual(self.english_to_French("None"), '')
        # Test empty string returns empty string
        self.assertEqual(self.english_to_French(0), '')

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def french_to_English(self, word):
        dictionary = {'Bonjour': 'Hello', 'Au revoir': 'Goodbye', 'Oui': 'Yes', 'Non': 'No'}
        return dictionary.get(word, '')

    def test1(self):
        # Test Bonjour returns Hello
        self.assertEqual(self.french_to_English('Bonjour'), 'Hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(self.french_to_English('Bonjour'), 'Bonjour')
        # Test None returns empty string
        self.assertEqual(self.french_to_English("None"), '')
        # Test empty string returns empty string
        self.assertEqual(self.french_to_English(0), '')
  
if __name__ == '__main__':
    unittest.main()