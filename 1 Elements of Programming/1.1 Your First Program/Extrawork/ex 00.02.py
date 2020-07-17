import sys
import stdio

T = float(sys.argv[1])  # temperature in Celsius degrees
v = float(sys.argv[2])  # wind speed in meters per second

v1 = v * 2.23694
v1 = v1 / 3.6
T1 = (T * 9 / 5) + 32
# todo convert Celsius degrees to Fahrenheit degrees
# todo convert meters per second to miles per hour

temperature = 33.74 + 0.6215 * T1 + (0.4275 * T1 - 35.75) * v1 ** 0.16
celsius = (temperature - 32) * 5 / 9
stdio.writeln(celsius)
# todo convert Fahrenheit degrees to Celsius degrees and print to console
# todo add usage
