with open('day09.txt', 'r') as f:
    arr = [int(line.strip()) for line in f]

n = len(arr)

# Part 1
pre = 25
idx = pre
sol = []
for idx in range(pre,n):
    sol.append(0)
    for i in range(pre):
        for j in range(pre):
            if (i != j) and (arr[idx-pre+i]+arr[idx-pre+j]==arr[idx]):
                sol[idx-pre] = 1

print(arr[sol.index(0)+pre])

# Part 2
idx = sol.index(0)+pre
num = arr[idx]

sol = []
for i in range(idx):
    con_sum = arr[i]
    cnt = 0
    while con_sum <= num:
        cnt += 1
        con_sum += arr[i+cnt]
        if con_sum == num:
            sol = arr[i:i + cnt]

print(min(sol)+max(sol))


