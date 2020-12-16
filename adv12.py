with open('day12.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)
arr = []

for i in range(n):
    arr.append(['',0])
    arr[i][0] = arr_str[i][:1]
    arr[i][1] = int(arr_str[i][1:])

# Part 1
position = [0,0]
rot = 0
for i in range(n):
    rot = rot % 4
    if arr[i][0] == 'F':
        if rot == 0:
            dir = 'E'
        elif rot == 1:
            dir =  'N'
        elif rot == 2:
            dir =  'W'
        elif rot == 3:
            dir =  'S'
    else:
        dir = arr[i][0]

    if dir == 'L':
        rot += arr[i][1]/90
    elif dir == 'R':
        rot -= arr[i][1]/90
    elif dir == 'E':
        position[0] += arr[i][1]
    elif dir == 'N':
        position[1] += arr[i][1]
    elif dir == 'W':
        position[0] -= arr[i][1]
    elif dir == 'S':
        position[1] -= arr[i][1]

print(abs(position[0])+abs(position[1]))


# Part 2
ship = [0,0]
wpoint = [10,1]

def rotate(arr1,arr2):
    rel_wpoint = [arr1[0] - arr2[0],arr1[1] - arr2[1]]
    old_x = rel_wpoint[0]
    old_y = rel_wpoint[1]
    if rot == 1:
        new_wpoint = [arr2[0] - old_y, arr2[1] + old_x]
    elif rot == 2:
        new_wpoint = [arr2[0] - old_x, arr2[1] - old_y]
    elif rot == 3:
        new_wpoint = [arr2[0] + old_y, arr2[1] - old_x]
    return new_wpoint

for i in range(n):
    dir = arr[i][0]
    if dir == 'L':
        rot = arr[i][1]/90
        wpoint = rotate(wpoint,ship)
    elif dir == 'R':
        rot = (-arr[i][1]/90) % 4
        wpoint = rotate(wpoint,ship)
    elif dir == 'E':
        wpoint[0] += arr[i][1]
    elif dir == 'N':
        wpoint[1] += arr[i][1]
    elif dir == 'W':
        wpoint[0] -= arr[i][1]
    elif dir == 'S':
        wpoint[1] -= arr[i][1]
    elif dir == 'F':
        rel_wpoint = [wpoint[0] - ship[0],wpoint[1] - ship[1]]
        ship[0] += arr[i][1] * rel_wpoint[0]
        ship[1] += arr[i][1] * rel_wpoint[1]
        wpoint[0] = ship[0] + rel_wpoint[0]
        wpoint[1] = ship[1] + rel_wpoint[1]

print(abs(ship[0])+abs(ship[1]))




