import math
import sys

import stdio

x1 = math.degrees(float(sys.argv[1]))
y1 = math.degrees(float(sys.argv[2]))
x2 = math.degrees(float(sys.argv[3]))
y2 = math.degrees(float(sys.argv[4]))
d = math.degrees(60) * (math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))
