#!/usr/bin/python3

from algo import primes, babygiant
from random import randrange, getrandbits

'''
simple illustration of diffie-hellman on integers modulo p
'''

'''
discrete log problem
A = g^a mod p where p is prime.
given p, g, A, find a
k is length of primes
'''
def dlog(k=16):
    #genprime
    p = primes.sample(k)
    g = randrange(2,p-1)
    a = getrandbits(k)
    a |= (1 << k - 1) #ensure msb is 1
    A = pow(g,a,p)
    return p, g, A

'''
diffie hellman key exchange problem
A = g^a mod p; B = g^b mod p
given p, g, A, B, find a or b
'''
def dhke(k=16):
    #genprime
    p = primes.sample(k)
    g = randrange(2,p-1)
    a = getrandbits(k)
    a |= (1 << k - 1)
    b = getrandbits(k)
    b |= (1 << k - 1)
    A = pow(g,a,p)
    B = pow(g,b,p)
    Sa = pow(B,a,p)
    Sb = pow(A,b,p)
    if(Sa != Sb):
        print("invalid shared key.")
        return 0,0,0,0
    print("shared key is %s" % hex(Sa))
    return p, g, A, B

if __name__ == "__main__":

    #p, g, A = dlog(16)
    #s = babygiant.solve(p,g,A)
    #print(p,g,A,':',s, g**s%p == A)

    # solving a 48-bit dhke takes roughly 1minute, 15seconds on i7-8750H 6 Cores @ 2.2GHz
    p, g, A, B = dhke(48)
    s = babygiant.solve(p,g,A)
    print(p,g,A,B, ':',s, pow(g,s,p) == A)
    print("attacker calculates shared key as %s" % hex( pow(B,s,p) ))



