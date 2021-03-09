#!/usr/bin/python3
import random

"""
Estimating pi with random numbers
"""

def estimatepi(n):
    npoints = 0
    ntotal = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        d = x**2 + y**2 #euclidean distance, don't care to sqrt
        if d <= 1:
            npoints += 1
        ntotal += 1
    # pi*r^2 / 2*r^2
    return 4*npoints/ntotal

#run
#estimatepi(3)
#estimatepi(30)
#estimatepi(300)

        
