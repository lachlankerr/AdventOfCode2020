'''
    Day 12: https://adventofcode.com/2020/day/12
'''

import re

NORTH = [1, 0]
SOUTH = [-1, 0]
EAST = [0, 1]
WEST = [0, -1]
LEFT = -1
RIGHT = 1

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day12input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
    '''

    direction_vector = EAST.copy() # starts facing east
    current_position = [0, 0]

    for line in lines:
        capture = re.match(r'([A-Z])(\d+)', line)
        action = capture.group(1)
        value = int(capture.group(2))

        if action == 'N':
            current_position = update_position(current_position, NORTH, value)
        elif action == 'S':
            current_position = update_position(current_position, SOUTH, value)
        elif action == 'E':
            current_position = update_position(current_position, EAST, value)
        elif action == 'W':
            current_position = update_position(current_position, WEST, value)
        elif action == 'L':
            direction_vector = change_direction_vector(direction_vector, LEFT, value)
        elif action == 'R':
            direction_vector = change_direction_vector(direction_vector, RIGHT, value)
        elif action == 'F':
            current_position = update_position(current_position, direction_vector, value)

    return abs(current_position[0]) + abs(current_position[1]) # since we start at 0,0 we can just do abs of both, not 53 or 174, too low

def change_direction_vector(direction_vector, direction, degrees):
    '''
    '''

    while degrees > 0:
        if direction == LEFT:
            if direction_vector[0] == 0: # checked
                direction_vector[0] = direction_vector[1]
                direction_vector[1] = 0
            else: 
                direction_vector[1] = direction_vector[0] * -1
                direction_vector[0] = 0
        elif direction == RIGHT:
            if direction_vector[0] == 1:
                direction_vector[1] = direction_vector[0]
                direction_vector[0] = 0
            else:
                direction_vector[0] = direction_vector[1] * -1
                direction_vector[1] = 0

        degrees -= 90

    return direction_vector

def update_position(current_position, direction_vector, value):
    '''
    '''

    current_position[0] += direction_vector[0] * value
    current_position[1] += direction_vector[1] * value

    return current_position

def part_two(lines):
    '''
    '''

    pass