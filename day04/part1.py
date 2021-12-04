#!/usr/bin/env python3

input = open('input.txt').read().splitlines()
input.reverse() # reverse so we can use .pop() later

def parse_row(row):
    return [ int(n) for n in row ]


numbers = parse_row(input.pop().split(','))
numbers.reverse()

boards = list()
none_row = [None] * 5

# init boards
while len(input) > 0:
    input.pop()
    board = list()
    for i in range(5):
        board.append(parse_row(input.pop().split()))
    boards.append(board)

def find_score():
    used_numbers = []
    while len(numbers) > 0:
        n = numbers.pop()
        used_numbers.append(n)
        for b in boards:
            found_number = False
            for i in range(25):
                if b[int(i/5)][i%5] == n:
                    b[int(i/5)][i%5] = None
                    found_number = True
                    break
            if found_number:
                # the board was modified, let's check if it won
                for i in range(5):
                    if b[i] == none_row or [b[j][i] for j in range(5)] == none_row:
                        # print(used_numbers)
                        print("Board %d won!" % (boards.index(b)+1))
                        return n * sum([sum([0 if v is None else v for v in r]) for r in b])

print(find_score())
            
                


