import sys

T = float(sys.argv[1])  # temperature in Celsius degrees
v = float(sys.argv[2])  # wind speed in meters per second

# todo convert Celsius degrees to Fahrenheit degrees
# todo convert meters per second to miles per hour
temperature = 33.74 + 0.6215 * T + (0.4275 * T - 35.75) * v ** 0.16
# todo convert Fahrenheit degrees to Celsius degrees and print to console
# todo add usage
