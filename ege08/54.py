import itertools


k = 0
for s, i in enumerate(itertools.product('СЛОН', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('О') <= 3:
        print(s, ss)
        k+=1
print(k)


