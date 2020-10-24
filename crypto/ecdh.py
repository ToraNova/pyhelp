#!/usr/bin/python3

from algo import primes, babygiant
from random import randrange, getrandbits
from gstruct import ecc

def dlog(ec, g):
    #genprime
    a = ec.getrandint()
    a |= (1 << k - 1) #ensure msb is 1
    A = ec.mul(a, g)
    return A

if __name__ == "__main__":

    k = 16
    k = 24 # 24 bit takes roughly 2 minutes
    a = 2
    b = 2
    p = primes.sample(k)

    c = ecc.Standard(a,b,p)
    p = ecc.Point(5,1)
    #c.computen(p)

    A = dlog(c, p)
    print("ecdlp instance (#E, g, A): %d %s %s" %(c.getord(), p,A))
    a = babygiant.ecsolve(c, p, A)
    if(a is not None):
        print("solved key: %d %s"%(a,c.mul(a,p)))
