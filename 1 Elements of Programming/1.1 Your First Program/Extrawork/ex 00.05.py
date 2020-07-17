import sys

import stdio

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

stdio.writeln((x > y > z) or (z > y > x))
