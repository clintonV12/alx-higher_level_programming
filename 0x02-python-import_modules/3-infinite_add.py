#!/usr/bin/python3
import sys
sum = 0
for arg in sys.argv:
    if arg == sys.argv[0]:
        continue
    else:
        sum += int(arg)
print(sum)
