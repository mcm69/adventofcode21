#!/usr/bin/env python3

input = [int(l) for l in open('input.txt').read().splitlines()]


total = 0

prevsum = 99999999
prev2 = input[0]
prev1 = input[1]

for i in range(2, len(input)):
    sum = prev2 + prev1 + input[i]
    if sum > prevsum:
        total+= 1
    prev2 = prev1
    prev1 = input[i]
    prevsum = sum

print(total)
