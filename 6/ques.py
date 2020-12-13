from collections import Counter

with open('input.txt', 'r') as file:
    inp = file.read().split('\n\n')
    inp = [inp[i].split('\n') for i in range(len(inp))]

# for each group, count the number of questions to which people answered yes
def num_yes(group):
    ans = ''.join(group)
    return len(list(set(ans)))

yes_answers = sum([num_yes(inp[i]) for i in range(len(inp))])

# questions to which everyone answered yes 
def everyone_answered_yes(i):
    everyone = len(i)
    ans = Counter(''.join(i))
    count = 0
    for k in ans.keys():
        if ans[k] == everyone:
            count += 1
    return count