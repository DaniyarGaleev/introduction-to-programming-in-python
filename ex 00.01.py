import math
import sys

import stdio

t = float(sys.argv[1])  # number of years (количество лет)
P = float(sys.argv[2])  # principal (начальная сумма денег)
r = float(sys.argv[3])  # interest rate (процентная ставка)

final_sum_of_money = P * (math.e ** ((r / 100) * t))
stdio.writeln(round(final_sum_of_money, 2))

# Usage (Запуск)
# > "ex 00.01.py" 0.5 100000 4.3
# 102173.28
# > "ex 00.01.py" 0.5 100000 5
# 102531.51
# > "ex 00.01.py" 0.5 100000 7.5
# 103821.2
