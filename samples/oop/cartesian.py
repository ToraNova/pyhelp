#!/usr/bin/python3

'''
point class of type cartesian
'''
class Point:

    # class variables
    cstype = "cartesian"

    # class methods
    # default, creates a point in origin
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def pos(self):
        return (self.x, self.y)

    def __str__(self):
        return '%s (%d, %d)' % (self.cstype, self.x, self.y)

    def __repr__(self):
        return 'repr: %s (%d, %d)' % (self.cstype, self.x, self.y)

class Line:
    def __init__(self, p1, p2):
        self.points = [p1, p2]

    def startpos(self):
        return self.points[0].pos()

    def endpos(self):
        return self.points[1].pos()
