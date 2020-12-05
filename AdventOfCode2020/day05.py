'''
    Day 05: https://adventofcode.com/2020/day/5
'''

import math

found_seat_list = []

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day05input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
        Calculates a list of seat ids and then returns the highest id
    '''

    for line in lines:
        row_str, column_str = line[:7], line[7:]
        row, column = binary_search(row_str, 127), binary_search(column_str, 7)

        seat_id = row * 8 + column

        found_seat_list.append(seat_id)

    return max(found_seat_list)

def part_two(lines):
    '''
        Finds the missing seat id based on all the other seat ids we have found in part one
    '''

    if (found_seat_list):
        first_seat = min(found_seat_list)
        last_seat = max(found_seat_list)

        actual_seat_list = list(range(first_seat, last_seat+1)) # create a list of all the actual seat numbers on the plane

        missing = list(set(actual_seat_list) - set(found_seat_list)) # find the missing numbers from our calculated seat list using sets

        return missing[0] # should only be one
    return None


def binary_search(str, max):
    '''
        Returns a number based on the binary search string.
    '''

    lower_range = 0
    upper_range = max 
    midpoint = (lower_range + upper_range) / 2 

    for char in str:
        if char == 'L' or char == 'F':
            upper_range = math.floor(midpoint)
        elif char == 'R' or char == 'B':
            lower_range = math.ceil(midpoint)
        midpoint = (lower_range + upper_range) / 2

    if lower_range == upper_range:
        return lower_range
    else:
        raise ValueError('Incorrect parameters supplied')
    

