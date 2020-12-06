with open('day3.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)
wid = len(arr_str[0])


# Part 1
x = 0
y = 0
trees = 0
for i in range(n-1):
    x += 3
    x = x % wid
    y += 1
    if arr_str[y][x]=='#':
        trees += 1

print(trees)

# Part 2
right = [1,3,5,7,1]
down = [1,1,1,1,2]

arr_trees = [0,0,0,0,0]
for j in range(5):
    x = 0
    y = 0
    for i in range(n-1):
        x += right[j]
        x = x % wid
        y += down[j]
        if y<=n:
            if arr_str[y][x]=='#':
                arr_trees[j] += 1

trees = 1
for i in arr_trees:
    trees = trees*i

print(trees)

