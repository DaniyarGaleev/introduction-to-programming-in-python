import sys

import stdio

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])
a = max(x, y, z)
b = min(x, y, z)
if x != a and x != b:
    stdio.writeln(x)
elif y != a and y != b:
    stdio.writeln(y)
elif z != a and z != b:
    stdio.writeln(z)
