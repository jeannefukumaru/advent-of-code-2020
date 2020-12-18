with open('input.txt', 'r') as file:
    input = file.readlines()
    input = [i.replace('\n', '') for i in input]
    input = [{i.split()[0]:i.split()[1]} for i in input]

inp = [{'nop':'+0'}, {'acc':'+1'}, {'jmp':'+4'},{'acc':'+3'},{'jmp': '-3'},{'acc':'-99'}, {'acc':'+1'},{'jmp':'-4'},{'acc': '+6'}]
seen = []
idx = 0
acc = 0
while idx not in seen:
    for k, v in input[idx].items():
        if k == 'acc':
            acc += int(v)
            print(acc)
            idx += 1
            print(idx)
            seen.append(idx)
        elif k == 'jmp':
            idx += int(v)
            seen.append(idx)
        elif k == 'nop':
            idx += 1
            seen.append(idx)
print(acc)