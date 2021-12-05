#!/usr/bin/env python3
input = open('input.txt').read().splitlines()

diagram = dict()
overlaps = 0

lines = []
for r in input:
    coords = [
        p.split(',')
        for p in r.split('->')
    ]

    (x1, y1) = int(coords[0][0]), int(coords[0][1])
    (x2, y2) = int(coords[1][0]), int(coords[1][1])

    if x1 == x2:
        # vertical line
        for y in range(min(y1, y2), max(y1, y2)+1):
            if not diagram.get(y):
                diagram[y] = dict()
            v = diagram[y].get(x1, 0)
            if v == 1:
                overlaps += 1
            diagram[y][x1] = v + 1
    
    if y1 == y2:
        # horizontal line
        if not diagram.get(y1):
            diagram[y1] = dict()
        for x in range(min(x1, x2), max(x1,x2)+1):
            v = diagram[y1].get(x, 0)
            if v == 1:
                overlaps += 1
            diagram[y1][x] = v + 1

print(overlaps)