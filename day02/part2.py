#!/usr/bin/env python3

input = open('input.txt').read().splitlines()

x = y = aim = 0

for l in input:
    s = l.split(' ')
    dir = s[0]
    u = int(s[1])
    if dir == "forward":
        x += u
        y += aim*u
    elif dir == "down":
        aim += u
    else: # "up"
        aim -= u

print(x*y)