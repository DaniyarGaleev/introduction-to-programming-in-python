import random
import sys

import stdio

n = int(sys.argv[1])
average = 0
min = 1
max = 0
for i in range(n):
    r = random.random()
    average += r
    if r > max: max = r
    if r < min: min = r
    stdio.writeln(r)

stdio.writeln('max = ' + str(max))

stdio.writeln('average = ' + str(average))

stdio.writeln('min = ' + str(min))

# Test 1:
# n = 10
# 0.396299172385971
# 0.15044253958258635
# 0.9815567032652128
# 0.01736829257152528
# 0.07846422275918274
# 0.22480832768917514
# 0.09939782027510391
# 0.6437633589533969
# 0.8831831711495237
# 0.7362364630398095
# max = 0.9815567032652128
# average = 4.211520071671487
# min = 0.01736829257152528

# Test 5:
# n = 5
# 0.05456500726388247
# 0.7159765182444784
# 0.29503564128938187
# 0.05536778924189256
# 0.8374497171584158
# max = 0.8374497171584158
# average = 1.9583946731980508
# min = 0.05456500726388247
