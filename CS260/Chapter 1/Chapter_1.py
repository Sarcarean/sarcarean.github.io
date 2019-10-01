import unittest

import Math_Fract


class TestFractionModule(unittest.TestCase):

    def test_addition(self):
        f1 = Math_Fract.Fraction(1,4)
        f2 = Math_Fract.Fraction(1,2)
        f3 = f1+f2
        self.assertEqual(f3, Math_Fract.Fraction(3,4))

    def test_str(self):
        f1 = Math_Fract.Fraction(1,2)
        self.assertEqual(str(f1), '1/2')

if __name__ == '__main__':
    #raise ValueError
    unittest.main(exit=False)


