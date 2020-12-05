'''
    Day 03: https://adventofcode.com/2020/day/3
'''

import re

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day03input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
    '''

    return count_trees_per_sloop(lines, 3, 1)

def part_two(lines):
    '''
    '''

    # not 20234789120
    return count_trees_per_sloop(lines, 1, 1) * count_trees_per_sloop(lines, 3, 1) * count_trees_per_sloop(lines, 5, 1) * count_trees_per_sloop(lines, 7, 1) * count_trees_per_sloop(lines, 1, 2)


def count_trees_per_sloop(lines, right_step, down_step):
    '''
    '''

    trees = 0
    position_right = 0
    position_down = 0

    mod_num = len(lines[0])

    for line in lines:
        if position_down % down_step:
            position_down += 1 # either repeat here or initialise position_down to -1
            continue
        if line[position_right % mod_num] == '#':
            trees += 1
        position_right += right_step
        position_down += 1

    return trees