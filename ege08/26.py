import itertools


k = 0
for s, i in enumerate(itertools.product('КУМА', repeat=5), 1):
    ss = ''.join(i)
    if (ss[0] in 'МК') and (ss[-1] in 'УА'):
        k+=1
        print(ss)
print(k)

