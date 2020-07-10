import random

import stdio

x = list()
for i in range(5):
    x.append(random.random())
x.sort()
stdio.writeln('Max = ' + str(max(x)))
stdio.writeln('average = ' + str(x[2]))
stdio.writeln('Min = ' + str(min(x)))
