import itertools


k = 0
for s, i in enumerate(itertools.product('ABCD', repeat=3), 1):
    ss = ''.join(i)
    if 'AD' in ss and 'BC' not in ss:
        k+=1
        print(ss)
print(k)

