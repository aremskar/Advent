# User code: 1175276-20201204-d7f5c55c

with open('day1.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)

arr=[]
for i in range(n):
    arr.append(int(arr_str[i]))

print(arr)

# Part 1
for i in range(n):
    for j in range(n):
        if arr[i]+arr[j]==2020:
            print(arr[i]*arr[j])

# Part 2
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[k]+arr[i]+arr[j]==2020:
                print(arr[i]*arr[j]*arr[k])

