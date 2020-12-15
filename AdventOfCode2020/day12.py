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
            if abs(direction_vector[0]) == 1:
                direction_vector[1] = direction_vector[0]
                direction_vector[0] = 0
            else:
                direction_vector[0] = direction_vector[1] * -1
                direction_vector[1] = 0

        degrees -= 90

    return direction_vector

# unit tests for above function
assert change_direction_vector(EAST.copy(), LEFT, 90) == NORTH
assert change_direction_vector(EAST.copy(), LEFT, 180) == WEST
assert change_direction_vector(EAST.copy(), LEFT, 270) == SOUTH
assert change_direction_vector(EAST.copy(), LEFT, 360) == EAST
    
assert change_direction_vector(NORTH.copy(), LEFT, 90) == WEST
assert change_direction_vector(NORTH.copy(), LEFT, 180) == SOUTH
assert change_direction_vector(NORTH.copy(), LEFT, 270) == EAST
assert change_direction_vector(NORTH.copy(), LEFT, 360) == NORTH
    
assert change_direction_vector(WEST.copy(), LEFT, 90) == SOUTH
assert change_direction_vector(WEST.copy(), LEFT, 180) == EAST
assert change_direction_vector(WEST.copy(), LEFT, 270) == NORTH
assert change_direction_vector(WEST.copy(), LEFT, 360) == WEST
    
assert change_direction_vector(SOUTH.copy(), LEFT, 90) == EAST
assert change_direction_vector(SOUTH.copy(), LEFT, 180) == NORTH
assert change_direction_vector(SOUTH.copy(), LEFT, 270) == WEST
assert change_direction_vector(SOUTH.copy(), LEFT, 360) == SOUTH

assert change_direction_vector(EAST.copy(), RIGHT, 90) == SOUTH
assert change_direction_vector(EAST.copy(), RIGHT, 180) == WEST
assert change_direction_vector(EAST.copy(), RIGHT, 270) == NORTH
assert change_direction_vector(EAST.copy(), RIGHT, 360) == EAST

assert change_direction_vector(NORTH.copy(), RIGHT, 90) == EAST
assert change_direction_vector(NORTH.copy(), RIGHT, 180) == SOUTH
assert change_direction_vector(NORTH.copy(), RIGHT, 270) == WEST
assert change_direction_vector(NORTH.copy(), RIGHT, 360) == NORTH

assert change_direction_vector(WEST.copy(), RIGHT, 90) == NORTH
assert change_direction_vector(WEST.copy(), RIGHT, 180) == EAST
assert change_direction_vector(WEST.copy(), RIGHT, 270) == SOUTH
assert change_direction_vector(WEST.copy(), RIGHT, 360) == WEST

assert change_direction_vector(SOUTH.copy(), RIGHT, 90) == WEST
assert change_direction_vector(SOUTH.copy(), RIGHT, 180) == NORTH
assert change_direction_vector(SOUTH.copy(), RIGHT, 270) == EAST
assert change_direction_vector(SOUTH.copy(), RIGHT, 360) == SOUTH

def update_position(current_position, direction_vector, value):
    '''
    '''

    current_position[0] += direction_vector[0] * value
    current_position[1] += direction_vector[1] * value

    return current_position

def part_two(lines):
    '''
    '''

    direction_vector = EAST.copy() # starts facing east
    current_position = [0, 0]
    waypoint = [1, 10]

    for line in lines:
        capture = re.match(r'([A-Z])(\d+)', line)
        action = capture.group(1)
        value = int(capture.group(2))

        if action == 'N':
            waypoint = update_position(waypoint, NORTH, value)
        elif action == 'S':
            waypoint = update_position(waypoint, SOUTH, value)
        elif action == 'E':
            waypoint = update_position(waypoint, EAST, value)
        elif action == 'W':
            waypoint = update_position(waypoint, WEST, value)
        elif action == 'L':
            direction_vector = change_direction_vector(direction_vector, LEFT, value)
        elif action == 'R':
            direction_vector = change_direction_vector(direction_vector, RIGHT, value)
        elif action == 'F':
            current_position = update_position(current_position, direction_vector, value)

    return abs(current_position[0]) + abs(current_position[1]) # since we start at 0,0 we can just do abs of both, not 53 or 174, too low