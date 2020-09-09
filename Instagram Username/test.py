import itertools

s='abcdefghijklmnopqrstuvwxyz._0123456789'

user_names4 = list(itertools.permutations(s,4))
user_names3 = list(itertools.permutations(s,3))
user_names2 = list(itertools.permutations(s,2))
user_names1 = list(itertools.permutations(s,1))

lst4 = []
lst3 = []
lst2 = []
lst1 = []

for s in user_names4:
    lst4.append("".join(s))

for s in user_names3:
    lst3.append("".join(s))

for s in user_names2:
    lst2.append("".join(s))

for s in user_names1:
    lst2.append("".join(s))
main_list = lst1 + lst2 + lst3 + lst4

f = open('output.txt', 'w+')

for s in main_list:
    f.write(s+'\n')
