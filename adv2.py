with open('day2.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)

for i in range(n):
    arr_str[i] = arr_str[i].split()

for i in range(n):
    arr_str[i][0] = arr_str[i][0].split('-')
    arr_str[i][0][0] = int(arr_str[i][0][0])
    arr_str[i][0][1] = int(arr_str[i][0][1])
    arr_str[i][1] = arr_str[i][1][0]

# Part 1
cnt = 0
for i in range(n):
    occ = arr_str[i][2].count(arr_str[i][1])
    if (occ>=arr_str[i][0][0] and occ<=arr_str[i][0][1]):
        cnt+=1

print(cnt)

# Part 2
cnt = 0
for i in range(n):
    let = arr_str[i][1]
    pas = arr_str[i][2]
    first = arr_str[i][0][0]-1
    second = arr_str[i][0][1]-1
    if len(pas)>=(first+1):
        if len(pas)>=(second+1):
            if (bool(pas[first]==let) ^ bool(pas[second]==let)):        # xor
                cnt+=1
        else:
            if pas[first]==let:
                cnt+=1

print(cnt)




