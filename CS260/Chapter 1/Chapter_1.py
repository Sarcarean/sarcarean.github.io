import unittest
import Math_Fract

class TestFractionModule(unittest.TestCase):
    """These are all of the unit tests that use the Fraction class"""
    def test_addition(self):
        f1 = Math_Fract.Fraction(1,4)
        f2 = Math_Fract.Fraction(1,2)
        f3 = f1+f2
        self.assertEqual(f3, Math_Fract.Fraction(3,4))

    def test_subtraction(self):
        f1 = Math_Fract.Fraction(3,8)
        f2 = Math_Fract.Fraction(1,4)
        f3 = f1-f2
        self.assertEqual(f3, Math_Fract.Fraction(1,8))

    def test_multiplication(self):
        f1 = Math_Fract.Fraction(1,2)
        f2 = Math_Fract.Fraction(4,5)
        f3 = f1*f2
        self.assertEqual(f3, Math_Fract.Fraction(2,5))

    def test_division(self):
        f1 = Math_Fract.Fraction(1,2)
        f2 = Math_Fract.Fraction(4,5)
        f3 = f1/f2
        self.assertEqual(f3, Math_Fract.Fraction(5,8))

    def test_str(self):
        f1 = Math_Fract.Fraction(1,2)
        self.assertEqual(str(f1), '1/2')

    def test_equal(self):
        f1 = Math_Fract.Fraction(1,2)
        f2 = Math_Fract.Fraction(1,2)
        self.assertEqual(f1==f2, True)

    def test_not_equal(self):
        f1 = Math_Fract.Fraction(1,2)
        f2 = Math_Fract.Fraction(3,2)
        self.assertEqual(f1!=f2, True)

    def test_less_than(self):
        f1 = Math_Fract.Fraction(1,8)
        f2 = Math_Fract.Fraction(1,4)
        self.assertEqual(f1<f2, True)

    def test_greater_than(self):
        f1 = Math_Fract.Fraction(7,8)
        f2 = Math_Fract.Fraction(1,4)
        self.assertEqual(f1>f2, True)


if __name__ == '__main__':
    unittest.main(exit=False)


