#!/usr/bin/python3
import random

"""
There are multiple chickens and rabbits in a cage.
There are 72 heads and 200 feet inside a cage
How many chickens and rabbits are there?
"""

def howmany_rabbits_chicks(nhead, nfeet):
    possible = []
    # i rabbit, j chick
    for i in range(nhead):
        j = nhead - i
        if(i*4 + j*2 == nfeet):
            possible.append((i,j))

    return possible

print(howmany_rabbits_chicks(72,200))

        
