#!/usr/bin/env python3

input = open('input.txt').read().splitlines()

x = y = 0

for l in input:
    s = l.split(' ')
    dir = s[0]
    u = int(s[1])
    if dir == "forward":
        x += u
    elif dir == "down":
        y += u
    else: # "up"
        y -= u

print(x*y)