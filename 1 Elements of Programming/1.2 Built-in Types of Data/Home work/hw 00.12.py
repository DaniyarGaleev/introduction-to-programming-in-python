import math
import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
if a >= a + b or b >= a + b:
    stdio.writeln(False)
else:
    stdio.writeln(True)
