import unittest
from translator import englishToFrench, frenchToEnglish

class TestSquare(unittest.TestCase): 
    def test1(self):
        """Unit Test for English to French Translation""" 
        self.assertEqual(englishToFrench(''))
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestSquare(unittest.TestCase): 
    def test1(self):
        """Unit Test for French to English Translation"""
        self.assertEqual(frenchToEnglish(''))
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
unittest.main()