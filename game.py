with open('input.txt', 'r') as file:
    inp = file.readlines()
    inp = [i.replace('\n', '') for i in inp]
    inp = [{i.split()[0]:i.split()[1]} for i in inp]

seen = []
idx = 0
acc = 0
while idx not in seen:
    for k, v in inp[idx].items():
        if k == 'acc':
            seen.append(idx)
            acc += int(v)
            idx += 1
        elif k == 'jmp':
            seen.append(idx)
            idx += int(v)
        elif k == 'nop':
            seen.append(idx)
            idx += 1
print(acc)