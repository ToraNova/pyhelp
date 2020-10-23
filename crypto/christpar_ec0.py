#!/usr/bin/python3

import gstruct.ecc as ecc
import numpy as np
import matplotlib.pyplot as plt

'''
coding example following lectures from Christof Parr
https://www.youtube.com/watch?v=vnpZXJL6QCQ
'''

if __name__ == "__main__":

    # plot y^2 = x^3 - 3x + 3 under real numbers
    # this is an invalid visual representation under modulo p operation

    a = 2
    b = 2
    p = 17

    c = ecc.Standard(a,b,p)

    vp = ecc.Point(5,1)
    print(vp, c.haspoint(vp))

    dvp = c.add(vp,vp)
    print(dvp, c.haspoint(dvp))

    tvp = c.add(vp,dvp)
    print(tvp, c.haspoint(tvp))

    tvp2 = c.add(dvp,vp)
    print(tvp2, c.haspoint(tvp2), tvp2.equals(tvp))

    p18 = ecc.Point(5,16)
    print(p18, c.haspoint(p18))

    p19 = c.add(p18, vp)
    print(p19, c.haspoint(p19))

    vp2 = c.add(p19, vp)
    print(vp2, c.haspoint(vp2), vp2.equals(vp))

    vp2 = c.negate(vp2)

    infp = c.add(vp2, vp)
    print(infp, c.haspoint(infp))

    #y, x = np.ogrid[-5:5:100j, -5:5:100j]
    #plt.contour(x.ravel(), y.ravel(), c.realplot(x,y), [0])
    #plt.grid()
    #plt.show()
