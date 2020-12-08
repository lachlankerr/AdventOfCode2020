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
        Gets the value of the accumulator when an instruction repeats itself
    '''

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
        Attempts to fix a broken instruction list by swapping exactly one nop -> jmp or jmp -> nop
    '''

    accumulator = 0

    no_loops = False

    swapped_instructions = []

    while not no_loops:
        no_loops = True
        swap_next_nop_or_jmp = True
        instruction_history = {}
        accumulator = 0
        i = 0
        while i < len(lines):
            instruction_history[i] = instruction_history.get(i, 0) + 1
            if instruction_history[i] > 1:
                no_loops = False
                break
            capture = re.match(r'(\w+) ([+-])(\d+)', lines[i])
            instruction = capture.group(1)
            sign = capture.group(2)
            value = capture.group(3)
            number = int(sign + value)
            if instruction == 'acc':
                accumulator += number
            elif instruction == 'jmp':
                if swap_next_nop_or_jmp and i not in swapped_instructions:
                    swap_next_nop_or_jmp = False
                    swapped_instructions.append(i)
                else:
                    i += number
                    continue
            elif instruction == 'nop':
                if swap_next_nop_or_jmp and i not in swapped_instructions:
                    swap_next_nop_or_jmp = False
                    swapped_instructions.append(i)
                    i += number
                    continue
            i += 1


    return accumulator