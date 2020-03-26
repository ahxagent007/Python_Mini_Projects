from sre_compile import isstring
import xlrd
import re


fileName1 = 'Kids related facebook groups.Liya.xlsx'
fileName2 = 'social-groups-LIYA001.xlsx'
# Opening the file as workbook
workbook1 = xlrd.open_workbook(fileName1)
workbook2 = xlrd.open_workbook(fileName2)

# Opening worksheet by its index
workSheet1 = workbook1.sheet_by_index(0)
workSheet2 = workbook2.sheet_by_index(0)

same = 0
nope = 0

yeslist = []
mainlis = []


for j in range(1,workSheet1.nrows):
    mainlis.append('#{0} SAME : {1}'.format(j,workSheet1.cell(j, 0).value))

for k in range(1, workSheet2.nrows):
    for j in range(1,workSheet1.nrows):

        str112 = workSheet1.cell(j, 0).value
        str700 = workSheet2.cell(k, 0).value

        s1 = re.sub(r"\s+", "", str112)
        s2 = re.sub(r"\s+", "", str700)

        if(s1 == s2):
            #print('#{0} SAME : {1}'.format(j,str112,str700))
            yeslist.append('#{0} SAME : {1}'.format(j,str112,str700))
            same += 1

        else:
            #print('#{0} NOPE : {1}'.format(j,str112))
            nope += 1

nolis = result = set(mainlis) - set(yeslist)

for n in nolis:
    print(n)

print('SAME = {0} NOPE = {1}'.format(same,nope))

