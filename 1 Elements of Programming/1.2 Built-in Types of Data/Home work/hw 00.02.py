import math
import stdio
import sys

alpha = float(sys.argv[1])
stdio.writeln(alpha)
stdio.writeln('cos^2(alpha) + sin^2(alpha) = ' + str(math.cos(alpha) ** 2 + math.sin(alpha) ** 2))
