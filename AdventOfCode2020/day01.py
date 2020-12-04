'''
    Day 01: https://adventofcode.com/2020/day/1
'''

magic_number = 2020

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day01input.txt') as f:
        lines = f.read().splitlines()

    lines = list(map(int, lines)) # convert list to ints

    lines.sort() # modifies in place

    return lines

def part_one(lines):
    '''
        Traverses the input lines and finds the two numbers that sum to 2020, then returns the product of them
    '''

    iterations = 0

    for i in range(len(lines)):
        for j in range(len(lines)):
            iterations += 1
            if lines[i] + lines[j] == magic_number:
                return lines[i] * lines[j], iterations # currently 373 iterations
            elif lines[i] + lines[j] > magic_number: # doesn't actually do anything for our list of numbers
                break 

def part_two(lines):
    '''
        Traverses the input lines and finds the three numbers that sum to 2020, then returns the product of them
    '''

    iterations = 0

    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                iterations += 1
                if lines[i] + lines[j] + lines[k] == magic_number:
                    return lines[i] * lines[j] * lines[k], iterations # currently 4611 iterations
                elif lines[i] + lines[j] + lines[k] > magic_number: # reduces iterations by 76446
                    break 