'''
    Day 07: https://adventofcode.com/2020/day/7
'''

import re

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day07input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
    '''

    for line in lines:
        capture = re.match(r'(.+) bags contain (.+)\.$', line)
            # split on ',' then do another regex for second capture