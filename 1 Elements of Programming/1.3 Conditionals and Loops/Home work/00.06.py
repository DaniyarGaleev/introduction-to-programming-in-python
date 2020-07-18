import sys

import stdio

n = int(sys.argv[1])
if 0 < n < 1000:
    stdio.writeln('1st Hello')
    if 1 < n:
        stdio.writeln('2nd Hello')
        if 2 < n:
            stdio.writeln('3rd Hello')
            if 3 < n:
                i = 4
                while i <= n:
                    stdio.writeln(str(i) + 'th Hello')
                    i = i + 1

# Test 1:
# n = 2
# 1st Hello
# 2nd Hello

# Test 2:
# n = 10
# 1st Hello
# 2nd Hello
# 3rd Hello
# 4th Hello
# 5th Hello
# 6th Hello
# 7th Hello
# 8th Hello
# 9th Hello
# 10th Hello
