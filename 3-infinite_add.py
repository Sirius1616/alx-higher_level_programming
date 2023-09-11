#!/usr/bin/python3
import sys

argv = sys.argv
sum = 0
for i in argv:
    if i == argv[0]:
        continue
    sum += int(i)
print(sum)

