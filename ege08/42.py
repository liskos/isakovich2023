import itertools


k = 0
for s, i in enumerate(itertools.product('ЛЕТО', repeat=4), 1):
    ss = ''.join(i)
    if 'Е' in ss:
        print(s, ss)
        k+=1
print(k)


