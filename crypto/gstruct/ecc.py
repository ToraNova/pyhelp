#!/usr/bin/python3

import math
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

    def copy(self):
        if(self.isinf()):
            return Point('inf')
        return Point(self._x, self._y)

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

    def __hash__(self):
        return hash((self._x,self._y,self._inf))

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
        self._n = self.boundn()

    def getord(self):
        return self._n

    # an upper bound on max # of elements based on Hasse's theorem
    # finding exact number is difficult, hence ppl use standard curves (NIST)
    def boundn(self,gmax=True):
        return int(self._p + 1 + 2*math.sqrt(self._p)) if gmax \
                else int(self._p + 1 - 2*math.sqrt(self._p))

    # untrivially compute cardinality of curve with base point 'base'
    # returns number of base points
    def computen(self,base):
        tp = base.copy()
        for n in range(self.boundn()):
            tp = self.add(tp, base)
            if(tp.isinf()):
                if(self.add(tp,base).equals(base)):
                    break
                else:
                    raise ValueError("curve %d %d %d is non-cyclic with base %s" % (self._a, self._b, self._p, base))
        self._n = n+2
        return n+2 #plus base and point at inf

    def getrandint(self, maxv = 2):
        if(maxv <= 2):
            maxv = self.getord() - 1
        return randrange(2, maxv)

    def mul(self,scalar,point):
        if(scalar == 0):
            return point.copy()
        return self._famul(scalar,point)

    # fast multiplication with doubling
    def _famul(self, scalar, point):
        tp = point.copy()
        if(tp.isinf()):
            return tp
        dt = int(math.log(scalar,2))
        for i in range(dt):
            tp = self._double(tp)
        for i in range(scalar-pow(2,dt)):
            tp = self._add(tp,point)
        return tp

    # naive multiplicative addition
    def _namul(self, scalar, point):
        tp = point.copy()
        for i in range(scalar-1):
            tp = self.add(tp, point)
        return tp

    def double(self,point):
        if(point.isinf()):
            return point.copy()
        return self._double(point)

    # unlikely to get inf element from doubling since cardinality is usually prime
    def _double(self,point):
        div = (2*point.gety()) % self._p
        num = ((3*pow(point.getx(),2)+self._a)) % self._p
        gcd, inv, _ = euclid.egcd_nr( div, self._p)
        s = ( num * inv ) % self._p
        if(gcd == self._p):
            return Point('inf')
        xo = (pow(s,2) - 2*point.getx()) % self._p
        yo = (s*(point.getx()-xo)-point.gety()) % self._p
        return Point(xo,yo)

    # group addition modulo p
    def add(self,p1,p2):
        if(p1.equals(p2)):
            # point doubling
            return self._double(p1)
        else:
            return self._add(p1,p2)

    def _add(self,p1,p2):
        # point adding
        if(p1.isinf()):
            return p2
        elif(p2.isinf()):
            return p1
        div = (p2.getx()-p1.getx()) % self._p
        num = (p2.gety()-p1.gety()) % self._p
        gcd, inv, _ = euclid.egcd_nr( div, self._p)
        s = ( num * inv ) % self._p
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
