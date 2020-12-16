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
