import re

with open('day04.txt', 'r') as f:
    arr_str = [line.strip() for line in f]

n = len(arr_str)

pas = ['']

j = 0
i = 0
while i<n:
    if arr_str[i] == '':
        pas.append(arr_str[i])
        j+=1
    else:
        pas[j] = pas[j]+' '+arr_str[i]
    i+=1

valid_pas = []
# Part 1
def check_valid(passport):
    if ('byr' in passport) and ('iyr' in passport) and ('eyr' in passport) and ('hgt' in passport) and ('hcl' in passport) and ('ecl' in passport) and ('pid' in passport):
        valid_pas.append(passport)
        return 1
    else:
        return 0

cnt = 0
for i in range(len(pas)):
    cnt += check_valid(pas[i])

print(cnt)

# Part 2

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.            
def check_valid_adv(passport):
    pas_dict = {}
    ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pas_dict['byr'] = int(passport[(passport.find('byr')+4):(passport.find('byr')+8)])
    pas_dict['iyr'] = int(passport[(passport.find('iyr')+4):(passport.find('iyr')+8)])
    pas_dict['eyr'] = int(passport[(passport.find('eyr')+4):(passport.find('eyr')+8)])
    pas_dict['hgt'] = passport[(passport.find('hgt')+4):(passport.find('hgt')+9)]
    pas_dict['hcl'] = passport[(passport.find('hcl')+4):(passport.find('hcl')+11)]
    pas_dict['ecl'] = passport[(passport.find('ecl')+4):(passport.find('ecl')+7)]
    pas_dict['pid'] = passport[(passport.find('pid')+4):(passport.find('pid')+13)]

    if not (pas_dict['byr']>=1920 and pas_dict['byr']<=2002):
        return 0
    elif not (pas_dict['iyr']>=2010 and pas_dict['iyr']<=2020):
        return 0
    elif not (pas_dict['eyr']>=2020 and pas_dict['eyr']<=2030):
        return 0
    elif not (re.search('1[5-9][0-9]cm',pas_dict['hgt']) or re.search('[5-7][0-9]in',pas_dict['hgt'])):  
        return 0
    elif not (re.search('#[a-f0-9]{6}',pas_dict['hcl'])):
        return 0
    elif not (pas_dict['ecl'] in ecl):
        return 0
    elif not (re.search('[0-9]{9}',pas_dict['pid'])):   
        return 0
    else:
        print(pas_dict)
        return 1


cnt = 0
for i in range(len(valid_pas)):
    cnt += check_valid_adv(valid_pas[i])

print(cnt)



