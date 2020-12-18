import re

with open('input.txt', 'r') as file:
    input = file.readlines()

# data cleaning 
# - remove newline characters from non-blank lines but preserve blank lines
# - join all entries together and re-split on blank lines so we get each persons details in a single list entry
# - get only entry without data by splitting on colon 
# put details into hash 
# for each entry in reference list, check for existence in details. return -1 if not exists else 1
# not okay if -1 exists, okay if 1 

input_remove_newlines = []
for i in input:
    if len(i) > 1:
        input_remove_newlines.append(i.replace('\n', ''))
    else:
        input_remove_newlines.append(i)

input_join_entries = ','.join(input_remove_newlines)
input_clean = input_join_entries.split(',\n,')
input_clean = [i.replace(',', ' ') for i in input_clean]
input_clean = [i.split() for i in input_clean]

details_regex = re.compile('[a-z]{3}:')
details_ls = [details_regex.findall(i) for i in input_clean]

def hash_details(entry):
    hsh = {}
    for e in entry:
        hsh[e] = 1
    return hsh

details_ls = [hash_details(entry) for entry in details_ls]

reference_list = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

result = []
for d in details_ls:
    tally = []
    for r in reference_list:
        tally.append(d.get(r, -1))
    if -1 not in tally:
        result.append(details_ls.index(d))
print(len(result))

# def validate_passport_fields(input_clean):
#     passports = []
#     for person in input_clean:
#         passports.append(dict(data.split(':') for data in person))
#     sum = 0
#     for person in passports:
#         if all(key in person.keys() for key in ["byr","iyr","eyr","hgt","hcl","ecl","pid"])
#     sum += 1
#     return sum

# part 2 

# byr - four digits between 1920 and 2002 
# iyr - four digits, between 2010 and 2020 
# eyr - four digits, between 2020 and 2030 
# height - if cm, between 150 and 193, if in, at least 59 and 193 
# hcl - # followed by exactly six characters 0-9 or a-f 
# ecl - exactly one of amb blu, brn, gry, grn, hzl, oth
# pid - nine digit number including leading zeros 
# cid - ignored, missing or not 

def byr_check(byr_str: str) -> bool:
    field = int(byr_str.split(':')[1])
    return 1 if field in range(1920, 2003) else -1

def iyr_check(iyr_str: str) -> bool:
    field = int(iyr_str.split(':')[1])
    return 1 if field in range(2010, 2021) else -1 

def eyr_check(eyr_str: str) -> bool:
    field = int(eyr_str.split(':')[1])
    return 1 if field in range(2020, 2031) else -1 

def hgt_check(hgt_str: str) -> bool:
    if hgt_str.endswith('cm'):
        field = int(hgt_str.split(':')[1].replace('cm', ''))
        return 1 if field in range(150, 194) else -1 
    elif hgt_str.endswith('in'):
        field = int(hgt_str.split(':')[1].replace('in', ''))
        return 1 if field in range(59, 194) else -1 
    return -1 

def hcl_check(hcl_str: str) -> bool:
    field = hcl_str.split(':')[1]
    regex = re.compile(r'^#[0-9a-f]{6}$')
    return 1 if bool(regex.match(field)) else -1 

def ecl_check(ecl_str: str) -> bool:
    ecl_ls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    field = ecl_str.split(':')[1]
    return 1 if field in ecl_ls else -1 

def pid_check(pid_str: str) -> bool:
    field = pid_str.split(':')[1]
    regex = re.compile(r'^[0-9]{9}$')
    return 1 if bool(regex.match(field)) else -1 

input_checks = []
for inpt in input_clean:
    valid = []
    entries = inpt.split(' ')
    for e in entries:
        if e.startswith('byr'):
            valid.append(byr_check(e))
        elif e.startswith('iyr'):
            valid.append(iyr_check(e))
        elif e.startswith('eyr'):
            valid.append(eyr_check(e))
        elif e.startswith('hgt'):
            valid.append(hgt_check(e))
        elif e.startswith('hcl'):
            valid.append(hcl_check(e))
        elif e.startswith('ecl'):
            valid.append(ecl_check(e))
        elif e.startswith('pid'):
            valid.append(pid_check(e))
    if -1 not in valid:
        input_checks.append('ok')

valid_passports = []

values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for person in passports:
    if (1920 <= int(person['byr']) <= 2002
            and (2010 <= int(person['iyr']) <= 2020)
            and (2020 <= int(person['eyr']) <= 2030)
            and
            ((person['hgt'][-2:] == 'cm' and 150 <= int(person['hgt'][:-2]) <= 193)
             or (person['hgt'][-2:] == 'in' and 59 <= int(person['hgt'][:-2]) <= 76))
            and (re.match(r'#[\da-f]{6}', person['hcl']))
            and (person['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            and (re.match(r'\d{9}', person['pid']))):
        valid_passports.append(person)