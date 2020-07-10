import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
stdio.writeln(((not (bool(a) and bool(b))) and (bool(a) or bool(b))) or ((bool(a) and bool(b)) or (not (bool(a) or bool(b)))))
