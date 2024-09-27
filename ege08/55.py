import itertools


k = 0
for s, i in enumerate(itertools.product('ЖИРАФ', repeat=6), 1):
    ss = ''.join(i)
    if 0 < ss.count('А') <= 4:
        print(s, ss)
        k+=1
print(k)


