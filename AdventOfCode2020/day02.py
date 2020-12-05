'''
    Day 02: https://adventofcode.com/2020/day/2
'''

import re

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day02input.txt') as f:
        lines = f.read().splitlines()

    return lines

def regex_lines(lines, function):
    '''
        Calculates the amount of valid passwords from the given list
    '''

    regex_string = "(\d+)-(\d+) (\w): (\w+)"

    valid_passwords = 0

    for line in lines:
        capture = re.search(regex_string, line)
        if function(capture.group(1), capture.group(2), capture.group(3), capture.group(4)):
            valid_passwords += 1
    
    return valid_passwords

def is_password_valid_part_one(min, max, letter, password):
    '''
        Determines if the given password is valid based on the required number of occurences of letter
    '''

    count = password.count(letter)
    return int(min) <= count <= int(max)
        
def is_password_valid_part_two(first_position, second_position, letter, password):
    '''
        Determines if the given password is valid based on the position of a specific letter
    '''

    if password[int(first_position)-1] == letter and password[int(second_position)-1] != letter:
        return True
    elif password[int(first_position)-1] != letter and password[int(second_position)-1] == letter:
        return True
    return False