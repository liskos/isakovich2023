import itertools


k = 0
for s, i in enumerate(itertools.product('КОМАР', repeat=4), 1):
    ss = ''.join(i)
    if ss.count('А') <= 3:
        print(s, ss)
        k+=1
print(k)


