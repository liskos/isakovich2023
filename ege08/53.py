import itertools


k = 0
for s, i in enumerate(itertools.product('МУХА', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('У') <= 3:
        print(s, ss)
        k+=1
print(k)


