import random
import stdio
import sys

T = float(sys.argv[1])
v = float(sys.argv[2])
if T <= 50 and 3<= v <= 120:
    stdio.writeln(33.74 + 0.6215 * T + (0.4275 * T - 35.75) * v ** 0.16)
