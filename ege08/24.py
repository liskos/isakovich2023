import itertools


k = 0
for s, i in enumerate(itertools.product('МАРТ', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('Р') == 2:
        k+=1
        print(ss)
print(k)

