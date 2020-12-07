import math

with open('day5.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)

# Part 1
row=[]
col=[]
for i in range(n):
    row.append(0)
    col.append(0)
    for j in range(7):
        if arr_str[i][j]=='B':
            row[i]+=math.pow(2,6-j)
    for j in range(3):
        if arr_str[i][j+7]=='R':
            col[i]+=math.pow(2,2-j)

seat_IDs = []
for i in range(n):
    seat_IDs.append(row[i]*8+col[i])

print(max(seat_IDs))

# Part 2
seat_IDs.sort()

i = seat_IDs[0]
while i in seat_IDs:
    i+=1
print(i)

