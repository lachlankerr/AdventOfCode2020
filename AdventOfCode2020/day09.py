'''
    Day 09: https://adventofcode.com/2020/day/9
'''

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day09input.txt') as f:
        lines = f.read().splitlines()

    lines = list(map(int, lines)) # convert list to ints

    return lines

def part_one(lines):
    '''
        Finds the number in the list that cannot be made from the previous `preamble_size` numbers.
    '''

    preamble = []
    preamble_size = 25

    for line in lines:
        if len(preamble) < preamble_size:
            preamble.append(line)
        else:
            if not check_preamble(preamble, line):
                part_one_result = line
                return line 
            else:
                preamble.pop(0)
                preamble.append(line)

    pass

def check_preamble(preamble, num):
    '''
        Checks if the given num is a product of two numbers in the preamble.
    '''

    for a in preamble:
        for b in preamble:
            if a + b == num:
                return True

    return False

def part_two(lines):
    '''
        Finds a contiguous set of at least two numbers that sum to the result of part_one, then returns the sum of the smallest and largest number in this contiguous set.
    '''

    part_one_result = part_one(lines)

    preamble = []
    preamble_size = 2
    
    i = 0
    while i < len(lines):
        if len(preamble) < preamble_size:
            preamble.append(lines[i])
        else:
            if sum(preamble) == part_one_result:
                return min(preamble) + max(preamble) 
            else:
                preamble.pop(0)
                preamble.append(lines[i])
        if i == len(lines) -1 and preamble_size < i:
            preamble_size += 1
            preamble = []
            i = 0
            continue
        i += 1

    pass
