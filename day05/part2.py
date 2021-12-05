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
    
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    xmin = min(x1, x2)
    xmax = max(x1, x2)

    if x1 == x2:
        # vertical line
        for y in range(ymin, ymax+1):
            if not diagram.get(y):
                diagram[y] = dict()
            v = diagram[y].get(x1, 0)
            if v == 1:
                overlaps += 1
            diagram[y][x1] = v + 1
    
    elif y1 == y2:
        # horizontal line
        if not diagram.get(y1):
            diagram[y1] = dict()
        for x in range(xmin, xmax+1):
            v = diagram[y1].get(x, 0)
            if v == 1:
                overlaps += 1
            diagram[y1][x] = v + 1

    else:
        # diagonal line
        for y in range(ymin, ymax+1):
            if not diagram.get(y):
                diagram[y] = dict()
        # diagonal line types:
        #   1      2      3      4
        # 1 . .  . . 3  3 . .  . . 1
        # . 2 .  . 2 .  . 2 .  . 2 .
        # . . 3  1 . .  . . 1  3 . .
        # 1: x1 < x2, y1 < y2
        # 2: x1 < x2, y1 > y2
        # 3: x1 > x2, y1 > y2
        # 4: x1 > x2, y1 < y2
        if (x1 >= x2 and y1 >= y2) or (x1 <= x2 and y1 <= y2):
            # line type 1 or 3 (direction right-down)
            for i in range(0, xmax-xmin+1):
                v = diagram[ymin+i].get(xmin+i, 0)
                if v == 1:
                    overlaps += 1
                diagram[ymin+i][xmin+i] = v + 1
        else:
            # line type 2 or 4 (direction right-up)
            for i in range(0, xmax-xmin+1):
                v = diagram[ymax-i].get(xmin+i, 0)
                if v == 1:
                    overlaps += 1
                diagram[ymax-i][xmin+i] = v + 1

print(overlaps)