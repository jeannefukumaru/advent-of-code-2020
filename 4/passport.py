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
        result.append('ok')
print(len(result))

# part 2 

# byr - four digits between 1920 and 2002 
# iyr - four digits, between 2010 and 2020 
# eyr - four digits, between 2020 and 2030 
# height - if cm, between 150 and 193, if in, at least 59 and 193 
# hcl - # followed by exactly six characters 0-9 or a-f 
# ecl - exactly one of amb blu, brn, gry, grn, hzl, oth
# pid - nine digit number including leading zeros 
# cid - ignored, missing or not 

for inpt in input_clean:
    entries = inpt.split(' ')

def byr_check(byr_str: str) -> bool:
    
    return True 

