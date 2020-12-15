'''
    Day 11: https://adventofcode.com/2020/day/11
'''

height = 0
width = 0

positions_to_check = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

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
    global height
    global width

    seats_changed = 1

    height = len(lines)
    width = len(lines[0])

    while seats_changed != 0:
        lines, seats_changed = apply_rules(lines, adjacent_occupied_part_one, 4)

    num_occupied = 0

    for line in lines:
        num_occupied += line.count('#')

    return num_occupied

def part_two(lines):
    '''
    '''    
    global height
    global width

    seats_changed = 1

    height = len(lines)
    width = len(lines[0])

    while seats_changed != 0:
        lines, seats_changed = apply_rules(lines, adjacent_occupied_part_two, 5)

    num_occupied = 0

    for line in lines:
        num_occupied += line.count('#')

    return num_occupied

def apply_rules(lines, function, occupied_rule):
    '''
    '''

    result = lines.copy()

    seats_changed = 0

    row = 0
    while row < height:
        col = 0
        while col < width:
            if lines[row][col] == '.':
                col += 1
                continue
            occupied = function(lines, row, col)
            if lines[row][col] == 'L' and occupied == 0:
                result[row] = result[row][:col] + '#' + result[row][col + 1:]
                seats_changed += 1
            elif lines[row][col] == '#' and occupied >= occupied_rule:
                result[row] = result[row][:col] + 'L' + result[row][col + 1:]
                seats_changed += 1
            col += 1
        row += 1

    return (result, seats_changed)

def adjacent_occupied_part_one(lines, row, col):
    '''
    '''

    occupied_seats = 0

    for position in positions_to_check:
        x = row + position[0]
        y = col + position[1]

        if x < 0 or y < 0 or x >= height or y >= width:
            continue

        if lines[x][y] == '#':
            occupied_seats += 1

    return occupied_seats

def adjacent_occupied_part_two(lines, row, col):
    '''
    '''

    occupied_seats = 0

    for position in positions_to_check:
        x = row + position[0]
        y = col + position[1]

        if x < 0 or y < 0 or x >= height or y >= width:
            continue

        while lines[x][y] == '.':
            x += position[0]
            y += position[1]

            if x < 0 or y < 0 or x >= height or y >= width:
                break

        if x < 0 or y < 0 or x >= height or y >= width:
            continue

        if lines[x][y] == '#':
            occupied_seats += 1

    return occupied_seats

def adjacent_occupied_slow(lines, row, col):
    '''
    '''

    occupied_seats = 0

    i = row - 1 if row > 0 else 0
    while i <= row + 1 and i < height:
        j = col - 1 if col > 0 else 0
        while j <= col + 1 and j < width:
            if not (i == row and j == col): # must skip current seat
                if lines[i][j] == '#':
                    occupied_seats += 1
            j += 1
        i += 1

    return occupied_seats