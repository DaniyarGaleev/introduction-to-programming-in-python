import sys

import stdio

a = float(sys.argv[1])
b = float(sys.argv[2])
if 0 < a < 1 and 0 < b < 1:
    stdio.writeln('True')
else:
    stdio.writeln('False')

# Test 1
# a = 0.1 b = 0.2
# result = True

# Test 2
# a = 0.1 b = 1
# result = False

# Test 3
# a = 1 b = 0.2
# result = False

# Test 4
# a = 1 b = 1
# result = False

# Test 5
# a = 0 b = 0.2
# result = False

# Test 6
# a = 0.1 b = 0
# result = False

# Test 7
# a = 0 b = 0
# result = False
