'''
    Day 14: https://adventofcode.com/2020/day/14
'''

import re

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day14input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
    '''

    mask_list = []

    mem = {}

    for line in lines:
        if line.startswith('mask'):
            capture = re.match(r'mask = ([X10]+)', line)
            mask = list(map(int, list(capture.group(1).replace('X', '2'))))
            mask.reverse()
            mask_list = []
            for i, bit in enumerate(mask):
                if bit != 2:
                    mask_list.append((bit, i))
        else:
            capture = re.match(r'mem\[(\d+)\] = (\d+)', line)
            location = int(capture.group(1))
            value = int(capture.group(2))

            for bit, i in mask_list:
                value = set_bit(value, i, bit)

            mem[location] = value

    result = 0

    for key, value in mem.items():
        result += value

    return result

def set_bit(v, index, x):
    '''
        Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value.
    '''
    mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
    v &= ~mask          # Clear the bit indicated by the mask (if x is False)
    if x:
        v |= mask         # If x was True, set the bit indicated by the mask.
    return v            # Return the result, we're done.

def part_two(lines):
    '''
    '''

    pass