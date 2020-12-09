import pandas as pd 
from collections import Counter

# Part 1
with open('2-input.txt', 'r') as f:
    input = f.readlines()
    input = [i.replace('\n', '') for i in input]
    input = [i.replace(':', '') for i in input]
    input = [i.replace('-', ' ') for i in input]
input_df = pd.DataFrame(columns=['start', 'end', 'letter', 'string'])

for i in input:
    start, end, letter, string = i.split(' ')
    d = {'start': int(start), 'end': int(end), 'letter': letter, 'string': string}
    input_df = input_df.append(d, ignore_index=True)

valid = []
for index, row in input_df.iterrows():
    string_hash = Counter(row['string'])
    if string_hash[row['letter']] in range(row['start'], row['end']+1):
        valid.append(index)
print(len(valid))

# Part 2 
valid = 0
for index, row in input_df.iterrows():
    char_a = row['string'][row['start']-1]
    char_b = row['string'][row['end']-1]
    char_hash = Counter([char_a, char_b])
    if char_hash.get(row['letter'], -1) == 1:
        valid += 1
