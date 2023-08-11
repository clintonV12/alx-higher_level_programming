#!/usr/bin/python3
import sys

number = len(sys.argv) - 1
c = 0
if number > c:
    print('{} arguments:'.format(number))
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        c += 1
        print('{}: {}'.format(c, arg))
else:
    print('{} arguments.'.format(number))
