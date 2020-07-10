import sys

import stdio

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

stdio.writeln((x > y and y > z) or (z > y and y > x))
