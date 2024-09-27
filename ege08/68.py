import itertools


k = 0
for s, i in enumerate(itertools.permutations('123456'), 1):
    ss = ''.join(i)
    if '56' in ss or '65' in ss:
        print(s, ss)
        k+=1
print(k)


