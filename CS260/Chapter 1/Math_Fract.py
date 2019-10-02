def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    """A class that creates a fraction object"""
    def __init__(self, top, bottom):
        """The fraction class constructor"""
        if not type(top) != type(int):
            raise Exception("Numerator is not an integer")
        if not type(bottom) != type(int):
            raise Exception("Denominator is not an integer")
        if bottom<0:
            bottom = bottom*-1
            top = abs(top)*-1
        common = gcd(top,bottom)
        self.num = top//common
        self.den = bottom//common

    def show(self):
        """The fraction class constructor"""
        print(self.num,"/",self.den)

    def __str__(self):
        """The fraction class constructor"""
        return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        """The fraction class constructor"""
        return self.__str__

    def __add__(self, otherfraction):
        """Performs a fraction addition operation, returns a fraction"""
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __radd__(self, otherfraction):
        """Performs a fraction addition operation, returns a fraction"""
        return self.__add__(otherfraction)

    def __iadd__(self, otherfraction):
        """Performs a fraction addition operation, returns a fraction"""
        return self.__add__(otherfraction)

    def __sub__(self, otherfraction):
        """Performs a fraction subtraction, returns a fraction"""
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __mul__(self, otherfraction):
        """Performs a fraction mulitplication, returns a fraction"""
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)

    def __truediv__(self, otherfraction):
        """Performs a fraction division, returns a fraction"""
        newnum = self.num*otherfraction.den
        newden = self.den*otherfraction.num
        return Fraction(newnum,newden)

    def __eq__(self, other):
        """Returns bool result of equals"""
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __ne__(self, other):
        """Returns bool result of not equals"""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Returns bool result of less than"""
        first = self.num/self.den
        second = other.num/other.den
        return first<second

    def __gt__(self, other):
        """Returns bool result of greater than"""
        return not self.__lt__(other)

    def __le__(self, other):
        """Returns bool result of less than or equal"""
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        """Returns bool result of greater than or equal"""
        return self.__gt__(other) or self.__eq__(other)