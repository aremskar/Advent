import re

with open('day07.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)
arr_str[0].strip('.')

for i in range(n):
    arr_str[i] = arr_str[i].split(' contain ')

# Part 1
def check_bag(colour):
    for i in range(n):
        if colour in arr_str[i][1]:
            temp_arr.append(arr_str[i][0])
            check_bag(arr_str[i][0][:-4])

temp_arr = []
check_bag('shiny gold')

temp_arr = set(temp_arr)
print(len(temp_arr))

# Part 2
cnt = [0]
def check_bag_adv(colour):
    return 1
    # for i in range(n):
    #     if colour in arr_str[i][0]:
    #         arr_str[i][1] = arr_str[i][1].split(', ')
    #         for j in arr_str[i][1]:
    #             j = j.strip('bags. ')
    #             if j[:1].isalpha():
    #                 return int(1)
    #             else:
    #                 cnt[0] += int(j[:1])*check_bag_adv(j[2:])

cnt = check_bag_adv('shiny gold')
print(cnt)