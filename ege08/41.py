import itertools


k = 0
for s, i in enumerate(itertools.product('КРАН', repeat=3), 1):
    ss = ''.join(i)
    if 'А' in ss:
        print(s, ss)
        k+=1
print(k)


