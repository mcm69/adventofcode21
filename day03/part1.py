#!/usr/bin/env python3

input = open('input.txt').read().splitlines()

width = len(input[0])

one_counters = [0] * width

for l in input:
    for i in range(width):
        if l[i] == '1':
            one_counters[i] += 1

gamma = epsilon = ''

for i in range(width):
    if one_counters[i] > len(input)/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print("gamma: %s\nepsilon: %s\nanswer: %s" % (gamma, epsilon, int(gamma, 2)*int(epsilon, 2)))

