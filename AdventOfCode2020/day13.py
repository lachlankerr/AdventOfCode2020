'''
    Day 13: https://adventofcode.com/2020/day/13
'''

import re

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day13input.txt') as f:
        lines = f.read().splitlines()

    return lines

def part_one(lines):
    '''
        Gets the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus.
    '''

    earliest_timestamp = int(lines[0])

    bus_ids = lines[1].split(',')

    highest_mod = 0
    highest_bus_id = 0

    for bus in bus_ids:
        if bus == 'x':
            continue
        bus_id = int(bus)
        mod = earliest_timestamp % bus_id
        if mod > highest_mod:
            highest_mod = mod
            highest_bus_id = bus_id

    return highest_bus_id * (highest_bus_id - highest_mod)

def part_two(lines):
    '''
        Instant version, takes into account that all the numbers are prime, so can adjust the multiplier once we have found the correct time for a bus id
    '''
    
    lines[1] = lines[1].replace('x', '0')

    bus_ids = list(map(int, lines[1].split(',')))

    new_list = []
    for i, bus in enumerate(bus_ids):
        if bus != 0:
            new_list.append((bus, i))

    multiplier = new_list.pop(0)[0]
    time = multiplier

    for bus, i in new_list:
        while (time + i) % bus != 0:
            time += multiplier
        multiplier *= bus

    return time

def part_two_faster(lines):
    '''
        Doesn't use enumerate and skips all the 0s, uses tuples to hold the offset
    '''
    
    lines[1] = lines[1].replace('x', '0')

    bus_ids = list(map(int, lines[1].split(',')))

    dict = {}
    new_list = []
    for i, bus in enumerate(bus_ids):
        if bus != 0:
            new_list.append((bus, i))

    start = new_list.pop(0)[0]
    time = start

    found = 1

    while found:
        found = 0
        for bus in new_list:
            if time % bus[0] != bus[0] - bus[1]:
                found = 1
                break
        if found:
            time += start

    return time

def part_two_working(lines):
    '''
        First iteration, will eventually work but will take hours
    '''
    
    lines[1] = lines[1].replace('x', '0')

    bus_ids = list(map(int, lines[1].split(',')))

    start = bus_ids.pop(0)
    time = start

    found = 1

    while found:
        found = 0
        for i, bus in enumerate(bus_ids):
            if bus != 0:
                if time % bus != bus - (i + 1):
                    found = 1
                    break
        if found:
            time += start



    return time