import sys

import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if a == b == c:
    stdio.writeln('equal')
else:
    stdio.writeln('not equal')

# Test 1
# a = 1 b = 2 c = 1
# result = not equal

# Test 2
# a = 1 b = 1 c = 1
# result = equal
