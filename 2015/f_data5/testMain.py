import unittest
from main import checkprohibited,checkStringDouble,checkStringVowels



class testMain(unittest.TestCase):
    def test_Checkprohibit(self):
        string1 = "abmichae"
        string2 = "aamicdli"
        string3 = "michael"
        self.assertEqual(checkprohibited(string1), False)
        self.assertEqual(checkprohibited(string2), False)
        self.assertEqual(checkprohibited(string3), True)

    def test_checkdouble(self):
        string1 = "bbmichael"
        string2 = "micaakaba"
        string3 = "liendoo"
        string4 = "lieindo"
        self.assertEqual(checkStringDouble(string1), True)
        self.assertEqual(checkStringDouble(string2), True)
        self.assertEqual(checkStringDouble(string3), True)
        self.assertEqual(checkStringDouble(string4), False)

    def test_checkStringvowel(self):
        string1 = "maeli"
        string2 = "papichu"
        string3 = "hodei"
        string4 = "hoa"
        string5 = "mcfhswt"
        self.assertEqual(checkStringVowels(string1), True)
        self.assertEqual(checkStringVowels(string2), True)
        self.assertEqual(checkStringVowels(string3), True)
        self.assertEqual(checkStringVowels(string4), False)
        self.assertEqual(checkStringVowels(string5), False)

if __name__ == '__main__':
    unittest.main()


