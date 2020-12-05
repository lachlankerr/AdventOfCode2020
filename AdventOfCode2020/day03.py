'''
    Day 03: https://adventofcode.com/2020/day/3
'''

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
        Returns the number of trees encounted on slope 'Right 3, down 1'.
    '''

    return count_trees_per_sloop(lines, 3, 1)

def part_two(lines):
    '''
        Returns the product of trees encounted on all 5 slopes:
            Right 1, down 1.
            Right 3, down 1.
            Right 5, down 1.
            Right 7, down 1.
            Right 1, down 2.
    '''

    # not 20234789120
    return count_trees_per_sloop(lines, 1, 1) * count_trees_per_sloop(lines, 3, 1) * count_trees_per_sloop(lines, 5, 1) * count_trees_per_sloop(lines, 7, 1) * count_trees_per_sloop(lines, 1, 2)


def count_trees_per_sloop(lines, right_step, down_step):
    '''
        Counts the number of trees encounted using a specific slope
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