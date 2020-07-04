import math
import stdio
import sys

G = 6.67e-11
M1 = float(sys.argv[1])
M2 = float(sys.argv[2])
R = float(sys.argv[3])
F = G * M1 * M2 / (R**2)
stdio.writeln(F)
