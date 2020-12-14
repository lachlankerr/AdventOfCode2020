'''
    Day 11: https://adventofcode.com/2020/day/11
'''

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day11input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
    '''

    seats_changed = 1

    while seats_changed != 0:
        lines, seats_changed = apply_rules(lines)

    num_occupied = 0

    for line in lines:
        num_occupied += line.count('#')

    return num_occupied

def part_two(lines):
    '''
    '''

    pass

def apply_rules(lines):
    '''
    '''

    result = lines.copy()

    seats_changed = 0

    row = 0
    while row < len(lines):
        col = 0
        while col < len(lines[row]):
            if should_be_occupied(lines, row, col):
                #print(result[row])
                result[row] = result[row][:col] + '#' + result[row][col + 1:]
                #print(result[row])
                seats_changed += 1
            if should_be_empty(lines, row, col):
                result[row] = result[row][:col] + 'L' + result[row][col + 1:]
                seats_changed += 1
            col += 1
        row += 1

    return (result, seats_changed)

def should_be_occupied(lines, row, col):
    '''
    '''

    occupied_seats = 0

    if lines[row][col] == 'L':
        i = row - 1 if row > 0 else 0
        while i <= row + 1 and i < len(lines):
            j = col - 1 if col > 0 else 0
            while j <= col + 1 and j < len(lines[row]):
                if not (i == row and j == col):
                    if lines[i][j] == '#':
                        occupied_seats += 1
                j += 1
            i += 1
    else:
        return False

    return occupied_seats == 0

def should_be_empty(lines, row, col):
    '''
    '''

    occupied_seats = 0

    if lines[row][col] == '#':
        i = row - 1 if row > 0 else 0
        while i <= row + 1 and i < len(lines):
            j = col - 1 if col > 0 else 0
            while j <= col + 1 and j < len(lines[row]):
                if not (i == row and j == col):
                    blah = lines[i][j]
                    if lines[i][j] == '#':
                        occupied_seats += 1
                j += 1
            i += 1
    else:
        return False

    return occupied_seats >= 4