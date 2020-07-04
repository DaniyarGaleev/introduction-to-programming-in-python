import math
import sys

import stdio

t = float(sys.argv[1])  # number of years (количество лет)
P = float(sys.argv[2])  # principal (начальная сумма денег)
r = float(sys.argv[3])  # interest rate (проценты)
stdio.writeln(P * math.e ** ((r / 100) * t))

# Usage
# >"ex 00.01.py" 0.5 100000 4.3
# 102173.2790337382
# >"ex 00.01.py" 0.5 100000 5
# 102531.5120524429
# >"ex 00.01.py" 0.5 100000 7.5
# 103821.19970818251
