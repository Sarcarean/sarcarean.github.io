import unittest
import Math_Fract
from timeit import Timer


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


def test_fractions():
        f1 = Math_Fract.Fraction(1,2)
        f2 = Math_Fract.Fraction(5,2)

def computeGCD1(x, y): 
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 

def computeGCD2(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 

def computeGCD3(a,b): 
    if(b==0): 
        return a 
    else: 
        return computeGCD3(b,a%b) 


def test_1():
    for x in range(1000):
        computeGC1D(60,48)


if __name__ == '__main__':
    test_fractions()

    t1 = Timer("computeGCD1(60,48)", "from __main__ import computeGCD1")
    print("computeGC1D: ", t1.timeit(number=100000),"milliseconds")

    t2 = Timer("computeGCD2(60,48)", "from __main__ import computeGCD2")
    print("computeGCD2: ", t2.timeit(number=100000),"milliseconds")

    t3 = Timer("computeGCD3(60,48)", "from __main__ import computeGCD3")
    print("computeGCD3: ", t2.timeit(number=100000),"milliseconds")

    unittest.main(exit=False)


