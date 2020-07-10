import math
import sys

import stdio

alpha0 = float(sys.argv[1])
phi = float(sys.argv[2])
phi = math.radians(phi)
alpha = float(sys.argv[3])

x = alpha - alpha0
y = 0.5 * math.log((1 + math.sin(phi)) / (1 - math.sin(phi)))
y = math.degrees(y)
stdio.writeln('x = ' + str(x))
stdio.writeln('y = ' + str(y))
