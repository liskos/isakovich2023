import itertools


k = 0
for s, i in enumerate(itertools.product('ТОК', repeat=6), 1):
    ss = ''.join(i)
    if ss[0] == 'Т' or ss[0] == 'К':
        k+=1
        print(ss)
print(k)

