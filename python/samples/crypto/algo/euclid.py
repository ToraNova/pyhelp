#!/usr/bin/python3

def __swapgt(a,b):
    if(a>b):
        return b,a
    else:
        return a,b

'''
euclidean algorithm,
find greatest common divisor between a,b
assume b > a
'''
def gcd(a,b):
    a = abs(a)
    b = abs(b)
    a,b = __swapgt(a,b)
    if(a==0):
        return b
    t = b % a
    return a if t == 0 else gcd(a,t)

'''
non recursive variant
'''
def gcd_nr(a,b):
    a = abs(a)
    b = abs(b)
    a,b = __swapgt(a,b)
    if(a==0):
        return b
    while(b % a != 0):
        a,b = __swapgt(a,b)
        b = b % a
    return a


'''
extended euclid algorithm
returns the gcd and p,q such that ap + bq = egcd_nr(a,b)[0]
assume a < b, q > p
p => t, q => s
non-recursive version
'''
def egcd_nr(a,b):
    a = abs(a)
    b = abs(b)
    a,b = __swapgt(a,b)
    so = 1
    to = 0
    s = 0
    t = 1
    if(a==0):
        return b, 0, 1
    if(a==1):
        return a, 1, 0
    while(1):
        a,b = __swapgt(a,b)
        q = b//a
        m = (s,t)
        s = so - (q) * s
        t = to - (q) * t
        so = m[0]
        to = m[1]
        bo = b
        b = b%a
        a,b = __swapgt(a,b)
        if(a==0 or b%a == 0):
            break
    # gcd, coeff small int, coeff large int
    return a, t, s

'''
mod inverse wrapper
return z such that az = 1 mod b
'''
def modinv(a,b):
    a = a % b
    gcd, inv, _ = egcd_nr(a,b)
    return inv

if __name__ == "__main__":
    gcd_tv = [
            (24,60,12),
            (1071,462,21),
            (24,18,6),
            (15,20,5),
            (12,18,6),
            (4,6,2),
            (3,5,1),
            (3,2,1),
            (12,90,6),
            (978,89798763754892653453379597352537489494736,6),
            (1234567891011121314151617181920212223242526272829,1221,3),
            (3,0,3),
            (4,7,1),
            (0,0,0),
            (0,1,1),
            (0,-1,1),
            (1914,899,29),
    ]
    for v in gcd_tv:
        g = gcd_nr(v[0],v[1])
        print(g,v[2], g == v[2])

    egcd_tv = [
            (46, 240, 2, 47, -9),
            (1914, 899, 29, -17, 8),
            (81, 57, 3, 10, -7),
            (1, 17, 1, 1, 0),
            (2, 17, 1, 9, 0)
    ]

    for v in egcd_tv:
        g,p,q = egcd_nr(v[0],v[1])
        print(g,v[2],p,v[3],q,v[4], all([g==v[2],p==v[3],q==v[4]]))

    # trial : modulo inversion
    g,p,q = egcd_nr(15,26) # p is the inverse
    print(g,p,q, p*15+q*26==1)
    g,p,q = egcd_nr(7,31) # p is the inverse
    print(g,p,q, p*7+q*31==1)
