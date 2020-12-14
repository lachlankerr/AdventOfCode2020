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
        Gets the product of 1 jolt differences and 3 jolt differences for the total number of adapters.
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
        (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
        Increments a counter for each adapter based on how many paths there are to that adapter from the starting adapter. 
        The counter increases for the connected adapters based on the current adapters path count.
    '''

    lines.append(0)
    lines.sort()

    paths = [0] * len(lines)
    paths[0] = 1

    i = 0
    while i < len(lines):
        j = i + 1
        while j < len(lines) and lines[j] - lines[i] <= 3:
            paths[j] += paths[i]
            j += 1
        i += 1


    return paths[-1]

def part_two_recursion(lines):
    '''
        Eventually gets the result but is too slow
    '''

    lines.append(0)
    lines.sort()
    lines.append(lines[-1] + 3)
    arrangements = set()

    base = lines.copy()

    arrangements.add(','.join(list(map(str, base))))

    arrangements = recursion(arrangements, base)

    return len(arrangements)

def recursion(arrangements, adapters):
    '''
        Works but is too slow for input
    '''

    i = 1
    while i < len(adapters) - 1:
        if adapters[i+1] - adapters[i-1] <= 3:
            new = adapters.copy()
            new.remove(adapters[i])
            str_new = ','.join(list(map(str, new)))
            if str_new not in arrangements:
                arrangements.add(str_new)
                arrangements |= recursion(arrangements, new)
        i += 1

    return arrangements

