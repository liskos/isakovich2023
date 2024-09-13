import itertools


k = 0
for s, i in enumerate(itertools.product('ГОД', repeat=6), 1):
    ss = ''.join(i)
    if ss[0] != 'О' and ss[-1] != 'О':
        k+=1
        print(ss)
print(k)

