'''
    Day 07: https://adventofcode.com/2020/day/7
'''

import re
import queue

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

    bags_dictionary = {}

    bags_containing_shiny_gold = set()

    seen_bags = set()

    for line in lines:
        first_capture = re.match(r'(.+) bags contain (.+)\.$', line)
        parent_bag = first_capture.group(1)
        contents = first_capture.group(2).split(', ')
        for bag in contents:
            second_capture = re.match(r'(\d+) (.+) bags?', bag)
            inner_bags = bags_dictionary.get(parent_bag, [])
            if second_capture:
                inner_bag = second_capture.group(2)
                inner_bags.append(inner_bag)
                if inner_bag == 'shiny gold':
                    bags_containing_shiny_gold.add(parent_bag)

            bags_dictionary[parent_bag] = inner_bags

    while bags_containing_shiny_gold:
        current_bag = bags_containing_shiny_gold.pop()
        for key, value in bags_dictionary.items():
            if current_bag in value and current_bag not in seen_bags:
                bags_containing_shiny_gold.add(key)
        seen_bags.add(current_bag)


    return len(seen_bags)

def part_two(lines):
    '''
    '''

    pass