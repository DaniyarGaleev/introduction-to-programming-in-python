import sys

import stdio

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y0 = y - (14 - m) // 12
x = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31 * m0) // 12) % 7
if d0 == 1:
    stdio.writeln('Monday')
elif d0 == 2:
    stdio.writeln('Tuesday')
elif d0 == 3:
    stdio.writeln('Wednesday')
elif d0 == 4:
    stdio.writeln('Thursday')
elif d0 == 5:
    stdio.writeln('Friday')
elif d0 == 6:
    stdio.writeln('Saturday')
else:
    stdio.writeln('Sunday')
