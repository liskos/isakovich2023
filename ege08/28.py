import itertools


k = 0
for s, i in enumerate(itertools.product('КРАНТ', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('К') == 2:
        k+=1
        print(ss)
print(k)

