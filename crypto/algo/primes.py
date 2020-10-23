#!/usr/bin/python3

from random import randrange, getrandbits
'''
prime generation algorithm based on the following article
https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
'''

'''
miller-rabin algo to test primality of number
n - test number
k - number of test runs (this is a probabilistic test)
'''
def test(n, k=128):
    if n == 2:
        return True # 2 is the only even prime number
    elif n < 2 or n % 2 == 0:
        return False #reject even number, 0, 1
    # miller-rabin
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

'''
generate prime number candidate
b - bit lenght of prime candidate
returns an integer
'''
def _getcandid(b):
    # generate random bits
    p = getrandbits(b)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << b - 1) | 1
    return p

'''
obtain a prime number of b-bits
returns an integer
'''
def sample(b=1024):
    p = _getcandid(b)
    # keep generating while the primality test fail
    while not test(p, 128):
        p = _getcandid(b)
    return p

if __name__ == "__main__":
    import math
    print("miller-rabin primality test")
    p16 = sample(16)
    print("bitsize: %d, %d" % (math.log(p16,2)+1,p16))
    p256 = sample(256)
    print("bitsize: %d, %d" % (math.log(p256,2)+1,p256))


