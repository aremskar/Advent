with open('day06.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)

# Part 1
groups = ['']
j = 0
i = 0
while i<n:
    if arr_str[i] == '':
        groups[j] = sorted(groups[j])
        groups.append(arr_str[i])
        j+=1
    else:
        groups[j] = groups[j]+arr_str[i]
    i+=1

qs = 0
for i in range(len(groups)):
    qs += len(set(groups[i]))

print(qs)

# Part 2
groups = [[]]
j = 0
i = 0
while i<n:
    if arr_str[i] == '':
        groups.append([])
        j+=1
    else:
        groups[j].append(arr_str[i])
    i+=1

def check_letter(letter,str_array):
    for i in str_array:
        if not (letter in i):
            return 0
    return 1

m = len(groups)
qs = 0
for i in range(m):
    for j in groups[i][0]:
        qs += check_letter(j,groups[i][1:])

print(qs)



