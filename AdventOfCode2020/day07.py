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

    bags_dictionary = {}

    for line in lines:
        first_capture = re.match(r'(.+) bags contain (.+)\.$', line)
        parent_bag = first_capture.group(1)
        contents = first_capture.group(2).split(', ')
        for bag in contents:
            second_capture = re.match(r'(\d+) (.+) bags?', bag)
            inner_bags = bags_dictionary.get(parent_bag, {})
            if second_capture:
                inner_bag = second_capture.group(2)
                bag_count = second_capture.group(1)
                inner_bags[inner_bag] = bag_count

            bags_dictionary[parent_bag] = inner_bags

    return recursive_bag_total(bags_dictionary, 'shiny gold') - 1

def recursive_bag_total(dictionary, key):
    '''
    '''

    total_count = 0
    sub_bags = dictionary[key]

    for bag, count in sub_bags.items():
        total_count += int(count) * recursive_bag_total(dictionary, bag)
        #total_count += int(count)

    total_count += 1

    return total_count