with open('day11.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)
wid = len(arr_str[0])

# Part 1
arr = [[]]
for i in range(wid+2):
    arr[0].append('.')
for i in range(n):
    arr.append(['.'])
    for j in arr_str[i]:
        arr[i+1].append(j)
    arr[i+1].append('.')
arr.append([])
for i in range(wid+2):
    arr[n+1].append('.')

def check_seat(row, col):
    around_row = [row-1, row-1, row-1, row, row, row+1, row+1, row+1]
    around_col = [col-1, col, col+1, col-1, col+1, col-1, col, col+1]
    def _occ(char):
        return char == '#'
    if old_grid[row][col] == 'L' or old_grid[row][col] == '#':
        total_occ = 0
        for i in range(8):
            total_occ += _occ(old_grid[around_row[i]][around_col[i]])
        if total_occ == 0:
            return '#'
        elif total_occ >= 4:
            return 'L'
        else:
            return old_grid[row][col]
    else:
        return '.'

def check_grid():
    for i in range(1,n+1):
        for j in range(1,wid+1):
            new_grid[i][j] = check_seat(i,j)

old_grid = list(map(list, arr))
new_grid = list(map(list, arr))

check_grid()
while not old_grid == new_grid:
    old_grid = list(map(list, new_grid))
    check_grid()

cnt = 0
for i in range(len(new_grid)):
    cnt += new_grid[i].count('#')

print(cnt)

# Part 2
def check_seat_adv(row, col):
    def _occ(char):
        return char == '#'
    def _in_range(a,b):
        if a>0 and b>0 and a<n+1 and b<wid+1:
            return True
        else:
            return False
    def _check_dir(x,y):
        temp_x = x
        temp_y = y
        while _in_range(row+temp_x,col+temp_y) and old_grid[row+temp_x][col+temp_y] == '.':
            temp_x+=x
            temp_y+=y
        return _occ(old_grid[row + temp_x][col + temp_y])

    dir_row = [-1, -1, -1, 0, 0, 1, 1, 1]
    dir_col = [-1, 0, 1, -1, 1, -1, 0, 1]
    if old_grid[row][col] == 'L' or old_grid[row][col] == '#':
        total_occ = 0
        for i in range(len(dir_row)):
            total_occ += _check_dir(dir_row[i], dir_col[i])
        if total_occ == 0:
            return '#'
        elif total_occ >= 5:
            return 'L'
        else:
            return old_grid[row][col]
    else:
        return '.'

def check_grid_adv():
    for i in range(1,n+1):
        for j in range(1,wid+1):
            new_grid[i][j] = check_seat_adv(i,j)

old_grid = list(map(list, arr))
new_grid = list(map(list, arr))

check_grid_adv()
while not old_grid == new_grid:
    old_grid = list(map(list, new_grid))
    check_grid_adv()

cnt = 0
for i in range(len(new_grid)):
    cnt += new_grid[i].count('#')

print(cnt)