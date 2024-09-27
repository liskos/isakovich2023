import itertools


k = 0
for s, i in enumerate(itertools.product('КАТЕР', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('Р') >= 2:
        print(s, ss)
        k+=1
print(k)


