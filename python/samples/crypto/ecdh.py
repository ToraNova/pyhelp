#!/usr/bin/python3

from algo import primes, babygiant
from random import randrange, getrandbits
from gstruct import ecc

def dlog(ec, g):
    #genprime
    a = ec.getrandint()
    #a |= (1 << k - 1) #ensure msb is 1
    A = ec.mul(a, g)
    return A

def test(a=2,b=2,k=16):
    p = primes.sample(k)
    _test(a,b,p)

def _test(a=2,b=2,p=17):
    c = ecc.Standard(a,b,p)
    p = ecc.Point(5,1)
    #c.computen(p)

    A = dlog(c, p)
    print("ecdlp instance (#E, g, A): %d %s %s" %(c.getord(), p,A))
    a = babygiant.ecsolve(c, p, A)
    if(a is not None):
        print("solved key: %d %s"%(a,c.mul(a,p)))

if __name__ == "__main__":

    test(2,2,16)
