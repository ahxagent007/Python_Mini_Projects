

file = open('txt.txt', 'r')
i = 1;
for f in file:
    lst = f.split(' ')
    lst.pop(0)
    strr = ''
    for l in lst:
        strr += l+' '

    print(strr)
    new_f = open(str(i)+'.txt','w+')
    i += 1
    new_f.write(strr)