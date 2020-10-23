#!/usr/bin/python3

from random import randrange
from algo import euclid

class Point:

    def __init__(self, x, y=0):
        self._inf = type(x) is str and x == "inf"
        self._x = x
        self._y = y

    def isinf(self):
        return self._inf

    def equals(self,point):
        if(self.isinf() and point.isinf()):
            return True
        return self._x == point.getx() and self._y == point.gety()

    def getx(self):
        if(self.isinf()):
            return 'inf'
        return self._x

    def gety(self):
        if(self.isinf()):
            return 'inf'
        return self._y

    def __str__(self):
        return '(inf)' if self.isinf() else ('(%d,%d)' % (self._x, self._y))

'''
standard elliptic curve under the form
y^2 = x^3 + ax + b modulo p
where 4a^3 + 27b^2 not congruent to 0 mod p
'''
class Standard:

    def __init__(self,a,b,p):
        self._a = a
        self._b = b
        self._p = p

    def getord(self):
        return self._p

    # group addition modulo p
    def add(self,p1,p2):
        if(p1.isinf()):
            return p2
        elif(p2.isinf()):
            return p1

        if(p1.equals(p2)):
            # point doubling
            gcd, inv, _ = euclid.egcd_nr(2*p1.gety(), self._p)
            s = ((3*pow(p1.getx(),2)+self._a) * inv ) % self._p
        else:
            # point adding
            gcd, inv, _ = euclid.egcd_nr((p2.getx()-p1.getx()), self._p)
            s = (abs(p2.gety()-p1.gety()) * inv) % self._p
        if(gcd == self._p):
            # point at inf
            return Point('inf')
        xo = (pow(s,2) - p1.getx() - p2.getx()) % self._p
        yo = (s*(p1.getx()-xo)-p1.gety()) % self._p
        return Point(xo,yo)

    def negate(self, point):
        return Point(point.getx(), (self._p - point.gety()))

    def haspoint(self,point):
        tx = point.getx()
        ty = point.gety()
        return point.isinf() or pow(ty,2) % self._p == (pow(tx,3) + self._a * tx + self._b) % self._p

    def realplot(self,x, y):
        return pow(y, 2) - pow(x, 3) - x * self._a - self._b
