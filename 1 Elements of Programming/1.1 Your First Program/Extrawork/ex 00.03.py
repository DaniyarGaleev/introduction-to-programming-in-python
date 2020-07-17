import math
import sys

import stdio

x = float(sys.argv[1])
y = float(sys.argv[2])
stdio.writeln('Theta ' + str(math.atan2(y, x)))
stdio.writeln('Radius ' + str(math.sqrt(x**2 + y**2)))
