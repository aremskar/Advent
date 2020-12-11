with open('day10.txt', 'r') as f:
    arr = [int(line.strip()) for line in f]

n = len(arr)
arr.sort()

# Part 1
cnt_1 = 1
cnt_3 = 1
for i in range(n-1):
    if arr[i+1]-arr[i]==1:
        cnt_1+=1
    elif arr[i+1]-arr[i]==3:
        cnt_3+=1

print(cnt_1*cnt_3)


# Part 2
arr.append(0)
arr.sort()

groups = [[]]
num = 0
for i in range(len(arr)-1):
    groups[num].append(arr[i])
    if arr[i]+3==arr[i+1]:
        groups.append([])
        num += 1
groups[-1].append(arr[-1])


def analyse_group(group):
    if len(group) == 1:
        return 1
    elif len(group)<=4:
        return pow(2,len(group)-2)
    else:
        return pow(2,len(group)-2)-1

cnt = 1
for i in groups:
    cnt *= analyse_group(i)

print(cnt)



