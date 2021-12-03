#!/usr/bin/env python3

input = open('input.txt').read().splitlines()

width = len(input[0])

def find_value(bin_value):
    a = list(input)
    counter = 0
    while len(a) > 1:
        ones = 0
        for i in range(len(a)):
            if a[i][counter] == '1':
                ones += 1
        if ones >= len(a)/2:
            a = [l for l in a if l[counter] == bin_value]
        else:
            a = [l for l in a if l[counter] == str(1-int(bin_value))]
        counter += 1
    return a[0]

oxygen = find_value('1')
co2 = find_value('0')

print("oxygen: %s\nco2:    %s\nanswer: %s" % (oxygen, co2, int(oxygen, 2)*int(co2, 2)))
