import stdio
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])

if a % b == 0:
    stdio.writeln(True)
else:
    stdio.writeln(False)
