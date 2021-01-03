import re

#Data
f = open('/Users/macuser/Desktop/AdventOfCode/day4_entry.txt', 'r')
passeports = f.read()
f.close()
passeports = passeports.split('\n\n')

def convert_string_to_dict(s):
    d = {}
    s = s.replace('\n', ' ').split(' ')
    for el in s:
        el = el.split(':')
        d[el[0]] = el[1]
    return d

#Puzzle 1
def solution1(passeports):
    valid_passeport = 0
    required_entries = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for p in passeports:
        p = convert_string_to_dict(p)
        if all([entry in p for entry in required_entries]):
            valid_passeport += 1
    return valid_passeport


#Puzzle 2
def valid_passport(p):
    required_entries = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not all([entry in p for entry in required_entries]):
        return False
    cond1 = (int(p['byr']) >= 1920) and (int(p['byr']) <= 2002)
    cond2 = (int(p['iyr']) >= 2010) and (int(p['iyr']) <= 2020)
    cond3 = (int(p['eyr']) >= 2020) and (int(p['eyr']) <= 2030)
    cond4 = False
    if (p['hgt'][-2:] in ['cm', 'in']):
        if (p['hgt'][-2:] == 'cm') and (int(p['hgt'][:-2]) >= 150) and (int(p['hgt'][:-2]) <= 193):
            cond4 = True
        elif (p['hgt'][-2:] == 'in') and (int(p['hgt'][:-2]) >= 59) and (int(p['hgt'][:-2]) <= 76):
            cond4 = True   
    cond5 = bool(re.match('#' + 6*'[0-9a-f]', p['hcl']))
    cond6 = p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    cond7 = bool(re.match(9*'[0-9]', p['pid']) and len(p['pid']) == 9)

    return cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7

def solution2(passeports):
    valid_passports = 0
    for p in passeports:
        p = convert_string_to_dict(p)
        if valid_passport(p):
            valid_passports+=1
    return valid_passports

if __name__ == "__main__":
    print('-------------------------')
    print('Number of valid passeport in puzzle 1:', solution1(passeports))
    print('-------------------------')
    print('Number of valid passeport in puzzle 2:', solution2(passeports))
    print('-------------------------')