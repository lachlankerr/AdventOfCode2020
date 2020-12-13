'''
    Day 10: https://adventofcode.com/2020/day/10
'''

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day10input.txt') as f:
        lines = f.read().splitlines()

    lines = list(map(int, lines)) # convert list to ints

    return lines

def part_one(lines):
    '''
    '''

    lines.sort()

    difference_one = 0
    difference_three = 0
    previous = 0

    device_joltage_adapter = lines[-1] + 3 # highest joltage + 3

    lines.append(device_joltage_adapter)

    for line in lines:
        if line - previous == 1:
            difference_one += 1
        elif line - previous == 3:
            difference_three += 1
        previous = line


    return (difference_one, difference_three, difference_one * difference_three) 

def part_two(lines):
    '''
    '''

    pass