'''
    Day 06: https://adventofcode.com/2020/day/6
'''

import math

found_seat_list = []

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day06input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
        Counts the number of distinct yes votes for each group
    '''

    yes_count = 0
    group_set = set()

    lines.append('') # if input doesn't have an empty line at end then it misses the last group

    for line in lines:
        if not line:
            yes_count += len(group_set)
            group_set = set()
        else:
            for char in line:
                group_set.add(char)

    return yes_count

def part_two(lines):
    '''
        Counts the number of yes votes that everyone in that group voted for
    '''

    yes_count = 0
    group_dictionary = {}
    group_count = 0

    lines.append('') # if input doesn't have an empty line at end then it misses the last group

    for line in lines:
        if not line:
            for key, value in group_dictionary.items():
                if value == group_count:
                    yes_count += 1
            group_dictionary = {}
            group_count = 0
        else:
            for char in line:
                group_dictionary[char] = group_dictionary.get(char, 0) + 1
            group_count += 1

    return yes_count