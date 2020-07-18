import sys

import stdio

n = int(sys.argv[1])

power = 0

while pow(2, power) < n:
    stdio.writeln(pow(2, power))
    power += 1

# Test 1:
# n = 9
# 1
# 2
# 4
# 8

# Test 2:
# n = 2
# 1
