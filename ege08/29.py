import itertools


k = 0
for s, i in enumerate(itertools.product('КАНТ', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('К') == 2:
        k+=1
        print(ss)
print(k)

