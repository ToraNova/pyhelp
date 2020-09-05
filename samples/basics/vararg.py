
'''
This file showcases variable arguments on
both args and kwargs
'''

# a variable argument definition
def vara(*args):
    print(args)
    for a in args:
        print(type(a))

def varb(**kwargs):
    print(kwargs)
    for a in kwargs.items():
        print(a)

def varc(*args, **kwargs):
    pass

def multia(a, b):
    return a, b

def multia_hack(a,b):
    return (a,b)

def ugly(tag, a):
    print('%s: %s' %( tag,a))

def pretty(tag, *args):
    print('%s:'%tag, args)
    print('%s:'%tag, *args)

if __name__ == "__main__":
    vara('hi',1,3,2)
    varb(a='hi',b=1);

    varc(1)
    varc(1,2,3)
    varc('hi',1,2,3,a=3)
    varc(b=4)

    print(1,2,3,4)
    ugly('TING', 'hello');
    ugly('TING', 'hi');
    #ugly('TING', 'hi', 'you'); #fail

    pretty('TING','hello')
    pretty('TING',1,2,3)

    a, b = multia(1,2)
    print(a)
    print(b)

    t = multia_hack(1,2)
    print(t)
