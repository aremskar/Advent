with open('day08.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)

# Part 1
idx = 0
acc = 0
all_indices = []
while not idx in all_indices:
    all_indices.append(idx)
    if arr_str[idx][:3] == 'acc':
        acc += int(arr_str[idx][4:])
        idx += 1
    elif arr_str[idx][:3] == 'jmp':
        idx+=int(arr_str[idx][4:])
    elif arr_str[idx][:3] == 'nop':
        idx+=1

print(acc)

# Part 2
for i in range(n):
    arr_copy = arr_str[:]
    if arr_str[i][:3] == 'jmp':
        arr_copy[i] = 'nop' + arr_str[i][3:]
    elif arr_str[i][:3] == 'nop':
        arr_copy[i] = 'jmp' + arr_str[i][3:]

    idx = 0
    acc = 0
    all_indices = []
    while (not idx in all_indices) and idx<n:
        all_indices.append(idx)
        if arr_copy[idx][:3] == 'acc':
            acc += int(arr_copy[idx][4:])
            idx += 1
        elif arr_copy[idx][:3] == 'jmp':
            idx += int(arr_copy[idx][4:])
        elif arr_copy[idx][:3] == 'nop':
            idx += 1
    if idx == n:
        print(acc)