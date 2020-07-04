import random
import stdio
import sys

t = float(sys.argv[1])
P = float(sys.argv[2])
r = float(sys.argv[3])
e = 2.7182818284
stdio.writeln(P * e ** ((r / 100) * t))
