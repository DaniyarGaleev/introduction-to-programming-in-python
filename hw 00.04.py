import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
stdio.writeln((not (a < b)) and (not (a > b)))
stdio.writeln(bool(a == b))
