#!/usr/bin/env python3

input = open('input.txt').read().splitlines()

prev = 9999999
total = 0

for l in input:
    current = int(l)
    if current > prev:
        total+= 1
    prev = current

print(total)
