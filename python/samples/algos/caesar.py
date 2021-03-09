#!/usr/bin/python3
import string

"""
Can you decrypt this
tqxxa rduqzp.
"""

space = string.ascii_lowercase
plain = 'hello friend.'

k = 142

def encrypt(p, k):
    k = k % 26
    crypt = ''
    for c in p:
        i = space.find(c)
        if(i < 0):
            crypt += c
            continue
        i = (i+k)%len(space)
        crypt += space[i]
    return crypt

def decrypt(c, k):
    k = k % 26
    plain = ''
    for p in c:
        i = space.find(p)
        if(i < 0):
            plain += p
            continue
        i = (i-k)%len(space)
        plain += space[i]
    return plain

def brute(c):
    possible = []
    for i in range(len(space)):
        possible.append(decrypt(c, i))
    return possible

crypt = encrypt(plain, k)
print(crypt)
a = brute(crypt)
for i,cand in enumerate(a):
    print(i,cand)
