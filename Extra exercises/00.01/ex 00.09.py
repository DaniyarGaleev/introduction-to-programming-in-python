import sys

import stdio

r = float(sys.argv[1])
g = float(sys.argv[2])
b = float(sys.argv[3])
w = max(r / 255, g / 255, b / 255)
c = (w - (r / 255)) * w
m = (w - (g / 255)) * w
y = (w - (b / 255)) * w
k = 1 - w
stdio.writeln('C = ' + str(c))
stdio.writeln('M = ' + str(m))
stdio.writeln('Y = ' + str(y))
stdio.writeln('K = ' + str(k))
