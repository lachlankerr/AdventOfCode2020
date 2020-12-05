'''
    Day 04: https://adventofcode.com/2020/day/4
'''

import re

def read_input():
    '''
        Reads the input file and returns a list of all the lines
    '''

    lines = []
    with open('day04input.txt') as f:
        lines = f.read().splitlines()

    return lines

def lines_to_passport(lines, function):
    '''
        Converts lines to passport dictionaries, then returns the number of valid passports
    '''

    dictionary = {}

    valid_passports = 0

    lines.append('') # if input doesn't have an empty line at end then it misses the last passport

    for line in lines:
        if not line:
            if function(dictionary):
                valid_passports += 1
            dictionary = {}
        else:
            pair_list = line.split()
            for pair in pair_list:
                key_value = pair.split(':')
                dictionary[key_value[0]] = key_value[1]
     
    return valid_passports # not 244 too low

def check_valid_passport_part_one(dictionary):
    '''
        Checks if the expected fields are contained in the dictionary, no data validation
    '''

    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # 'cid'

    for field in expected_fields:
        if field not in dictionary:
            return False

    return True

def check_valid_passport_part_two(dictionary):
    '''
        Checks the expected fields are contained in the dctionary then does data validation on them
    '''

    return check_year(dictionary, 'byr', 1920, 2002) and \
           check_year(dictionary, 'iyr', 2010, 2020) and \
           check_year(dictionary, 'eyr', 2020, 2030) and \
           check_height(dictionary) and \
           check_hair(dictionary) and \
           check_eye(dictionary) and \
           check_passport_id(dictionary)

def check_year(dictionary, key, min, max):
    '''
        Makes sure the year is a valid number and between the min and max range
    '''

    year = dictionary.get(key, 0)

    return min <= int(year) <= max

def check_height(dictionary):
    '''
        Makes sure the height is cm or in and in the min and max range
    '''

    height = dictionary.get('hgt', '')
    
    capture = re.match('(\d+)(cm|in)$', height)
    if capture:
        if capture.group(2) == 'cm':
            return 150 <= int(capture.group(1)) <= 193
        elif capture.group(2) == 'in':
            return 59 <= int(capture.group(1)) <= 76

    return False

def check_hair(dictionary):
    '''
        Makes sure the hair colour is a valid hex colour code
    '''

    hair_colour = dictionary.get('hcl', '')

    return re.match('#[0-9a-f]{6}$', hair_colour)

def check_eye(dictionary):
    '''
        Makes sure the eye colour is a valid 3 letter colour string
    '''

    eye_colour = dictionary.get('ecl', '')

    return re.match('(amb|blu|brn|gry|grn|hzl|oth)$', eye_colour)

def check_passport_id(dictionary):
    '''
        Makes sure the passport id is a 9 digit integer
    '''

    passport_id = dictionary.get('pid', '')

    return re.match('(\d){9}$', passport_id)