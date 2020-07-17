import sys

import stdio

T = float(sys.argv[1])  # temperature in Celsius degrees
v = float(sys.argv[2])  # wind speed in meters per second

v1 = v * 2.23694  # wind speed in meters per second
v1 = v1 / 3.6
T1 = (T * 9 / 5) + 32  # temperature in Celsius degrees
if T < 50 and 3 < v < 120:
    temperature = 33.74 + 0.6215 * T1 + (0.4275 * T1 - 35.75) * v1 ** 0.16
    celsius = (temperature - 32) * 5 / 9
    stdio.writeln(celsius)
elif T > 50:
    stdio.writeln('Temperature is too big')
else:
    stdio.writeln('Velocity is too big')
