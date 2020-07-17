import math
import sys

import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
D = b ** 2 - 4 * a * c
if D >= 0:
    stdio.writeln((-b + math.sqrt(D)) / (2 * a))
    if D != 0:
        stdio.writeln((-b - math.sqrt(D)) / (2 * a))
else:
    stdio.writeln('Discriminant is lower than 0')

# Test 1
# a = 1 b = -2 c = 1
# result = 1.0

# Test 2
# a = 1 b = -3 c = 2
# result num 1 = 2.0
# result num 2 = 1.0


# Test 3
# a = 1 b = -2 c = 4
# result = Discriminant is lower than 0
