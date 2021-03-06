#!/usr/bin/python3

import math

'''
baby step giant step dlog solver
based on article
https://medium.com/asecuritysite-when-bob-met-alice/baby-step-giant-step-solving-discrete-logarithms-and-why-its-a-hard-problem-to-solve-62b11bbe3088
'''

'''
integers modulo n solver
given p, g, A, find a such that g**a mod p = A
'''
def solve(p, g, A):
    N = int(math.ceil(math.sqrt(p-1)))
    #N = int(-(-((p-1)**0.5)//1))
    bt = {}# Baby step.
    for i in range(N):
        # Fermat’s Little Theorem
        bt[pow(g, i, p)]=i
    c = pow(g, N * (p - 2), p)

    for j in range(N):
        y = (A * pow(c, j, p)) % p
        if y in bt:
            return j * N + bt[y]
    return None

if __name__ == "__main__":
    tv = [
            (53,5,22),
            (53,5,20),
            (41,2,5),
            (14947,7,777)
    ]
    for v in tv:
        s = solve(v[0],v[1],v[2])
        print(s, pow(v[1],s,v[0]) == v[2])


'''
elliptic curve group solver.
ec - a standard elliptic curve group structure
cord - the order of the curve (computen)
g - base point
A - public point
'''
def ecsolve( ec, g, A):
    p = ec.getord()
    N = int(math.ceil(math.sqrt(p)))
    bt = {}

    for i in range(N):
        bt[hash(ec.mul(i, g))] = i

    c = ec.mul(N, g)

    for j in range(N):
        y = ec.add( A, ec.negate(ec.mul(j, c)))
        hval = hash(y)
        if hval in bt:
            #print(j,N,bt[hval])
            return N + bt[hval] if j==0 else j*N + bt[hval]
            #return j * N + bt[hval]
            #return N + bt[hval]
    return None
