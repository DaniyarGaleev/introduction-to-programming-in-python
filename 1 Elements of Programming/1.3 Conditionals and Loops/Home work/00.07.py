import stdio

counter = 1

for i in range(1000, 2001):
    if counter < 6:
        stdio.write(str(i) + ' ')
        counter += 1
    else:
        stdio.writeln()
        counter = 1
