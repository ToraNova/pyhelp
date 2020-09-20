#!/usr/bin/python3

'''
an animal example for object oriented programming
'''
class Animal:
    def __init__(self, nl, nf):
        self.alive = True
        self.hungry = True
        self.nleg = nl
        self.nfin = nf
        self.__spirit = 'tingcute'
        self._lspirit = 'worms'

    def sound(self):
        print('fafafafa')

    def move(self):
        self.hungry = True

    def feed(self):
        self.hungry = False

    def ishungry(self):
        return self.hungry

    def canswim(self):
        return self.nfin >= 1

    def canwalk(self):
        return self.nleg >= 2

    def canjump(self):
        return self.nleg >= 1

    def cantrot(self):
        return self.nleg >= 4

    def isalive(self):
        return self.alive

    def kill(self):
        self.alive = False

class Fish(Animal):

    def __init__(self, color):
        super().__init__(0, 4)
        self.color = color

    def sound(self):
        print('boopboop')

class Tuna(Fish):
    def __init__(self, name):
        super().__init__('grey')
        self.name = name

    def sound(self):
        print('im tuna')

class Mammal(Animal):
    def __init__(self, nl, nf):
        super().__init__(nl, nf)

    def sound(self):
        print('errrrrr')

class Elephant(Mammal):
    def __init__(self, name):
        super().__init__(4, 0)
        self.name = name

    def sound(self):
        print('EHHHHHHHHHHHHHHHHH')

if __name__ == "__main__":
    # zoo example

    e = Elephant("dumbo")

    t1 = Tuna("gary")
    t2 = Tuna("boop")

    print(e.ishungry())
    e.sound()
    t1.sound()

    print(e.nleg)

    for a in dir(e):
        print(a)

    #print(e._Animal__spirit)

    t1.kill()
    print(t1.isalive())


