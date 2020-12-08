'''
    Day 08: https://adventofcode.com/2020/day/8
'''

import re

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day08input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
    '''

    instructions = ['acc', 'jmp', 'nop']

    instruction_history = {}

    accumulator = 0

    i = 0
    while i < len(lines):
        instruction_history[i] = instruction_history.get(i, 0) + 1
        if instruction_history[i] > 1:
            break
        capture = re.match(r'(\w+) ([+-])(\d+)', lines[i])
        instruction = capture.group(1)
        sign = capture.group(2)
        value = capture.group(3)
        number = int(sign + value)
        if instruction == 'acc':
            accumulator += number
        elif instruction == 'jmp':
            i += number
            continue
        #elif instruction == 'nop':
        #    continue
        i += 1

    return accumulator

def part_two(lines):
    '''
    '''

    pass