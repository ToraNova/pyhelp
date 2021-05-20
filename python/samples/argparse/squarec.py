#!/usr/bin/python3

# a simple argument parsing reference
# reference: https://docs.python.org/3/howto/argparse.html

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square (or cube) of a given number", type=int)
# store_true means if specified, its true, else it is false
parser.add_argument("-e", "--echo", help="additional text to echo onto the screen") # no default -> defaults to None
parser.add_argument("-c", "--cubing", help="cube instead of square", action="store_true")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="count", default=0)
args = parser.parse_args()

e = 2
if args.cubing:
    e = 3
if args.verbosity > 1:
    print("square of %d is %d" %(args.square, args.square**e))
elif args.verbosity > 0:
    print("%d x %d = %d" %(args.square, args.square, args.square**e))
else:
    print(args.square**e)

if args.echo is not None:
    print(args.echo)
