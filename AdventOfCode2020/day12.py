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
        Calculates the ships position based on the given actions.
        Returns the manhattan distance of the ships final position from the starting position.
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

def change_direction_vector(vector, direction, degrees):
    '''
        Changes our direction vector in 90 degree increments depending on the given direction.
    '''

    while degrees > 0:
        if direction == LEFT:
            if vector[0] == 0: # checked
                vector[0], vector[1] = vector[1], 0
            else: 
                vector[0], vector[1] = 0, vector[0] * -1
        elif direction == RIGHT:
            if abs(vector[0]) == 1:
                vector[0], vector[1] = 0, vector[0]
            else:
                vector[0], vector[1] = vector[1] * -1, 0

        degrees -= 90

    return vector

# unit tests for change_direction_vector function
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
        Updates the given position by a vector or position scalar.
    '''

    current_position[0] += direction_vector[0] * value
    current_position[1] += direction_vector[1] * value

    return current_position

def part_two(lines):
    '''
        Calculates the ships position based on the given actions.
        Uses a waypoint instead of a direction vector.
        Returns the manhattan distance of the ships final position from the starting position.
    '''

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
            direction_vector = rotate_waypoint(waypoint, LEFT, value)
        elif action == 'R':
            direction_vector = rotate_waypoint(waypoint, RIGHT, value)
        elif action == 'F':
            current_position = update_position(current_position, waypoint, value)

    return abs(current_position[0]) + abs(current_position[1]) # since we start at 0,0 we can just do abs of both, not 53 or 174, too low

def rotate_waypoint(waypoint, direction, degrees):
    '''
        Rotates the waypoint in 90 degree increments either left or right.
        We don't have to think about the ships position because the waypoint is just a relative position.
    '''

    while degrees > 0:
        if direction == LEFT:
            waypoint[0], waypoint[1] = waypoint[1], waypoint[0] * -1
        elif direction == RIGHT:
            waypoint[0], waypoint[1] = waypoint[1] * -1, waypoint[0]
        degrees -= 90

    return waypoint