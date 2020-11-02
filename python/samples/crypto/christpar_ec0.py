#!/usr/bin/python3

from algo import primes, babygiant, euclid
import gstruct.ecc as ecc
import numpy as np
import matplotlib.pyplot as plt
import algo

'''
coding example following lectures from Christof Parr
https://www.youtube.com/watch?v=vnpZXJL6QCQ

y^2 = x^3 + ax + b mod p
toy curve: a=2,b=2,p=17
generator (5,1), P
2P  = (6,3)
3P  = (10,6)
4P  = (3,1)
5P  = (9,16)
6P  = (16,13)
7P  = (0,6)
8P  = (13,7)
9P  = (7,6)
10P = (7,11)
11P = (13,10)
12P = (0,11)
13P = (16,4)
14P = (9,1)
15P = (3,16)
16P = (10,11)
17P = (6,14)
18P = (5,16)
19P = inf
20P = (5,1) = P
21P = 2P ...
'''

if __name__ == "__main__":

    # plot y^2 = x^3 - 3x + 3 under real numbers
    # this is an invalid visual representation under modulo p operation

    a = 2
    b = 2
    #p = primes.sample(16)
    p = 17
    print("prime: %d" % p)

    c = ecc.Standard(a,b,p)
    p = ecc.Point(5,1)

    tp = p.copy()
    for i in range(24):
        print(i+1,tp)
        tp = c.add(p,tp)

    print("naPmul", c._namul(9,p))
    print("faPmul", c._famul(9,p))

    c.computen(p)
    print("#E = %d"% c.getord())

    #ra = []
    #for _ in range(100):
    #    d = c.getrandint()
    #    #print("secret %d"%d)
    #    pub = c.mul(d, p)
    #    #print("public point %s"%pub)
    #    td = babygiant.ecsolve( c, p, pub)
    #    if td is not None:
    #        #print("cracked %d"%td)
    #        #print("cracked public %s"% c.mul(td,p))
    #        ra.append(c.mul(td,p).equals(pub))
    #print(all(ra))


    #y, x = np.ogrid[-5:5:100j, -5:5:100j]
    #plt.contour(x.ravel(), y.ravel(), c.realplot(x,y), [0])
    #plt.grid()
    #plt.show()
