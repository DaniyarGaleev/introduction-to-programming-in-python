import stdio
import sys
import math

x0 = float(sys.argv[1])
v0 = float(sys.argv[2])
t = float(sys.argv[3])
g = 9.80665
stdio.writeln(x0 + v0 * t + g * t**2 / 2)
