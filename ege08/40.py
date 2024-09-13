import itertools


k = 0
for s, i in enumerate(itertools.product('ABCX', repeat=5), 1):
    ss = ''.join(i)
    if ss[-1] == 'X' and 'X' not in ss[:-1] or 'X' not in ss:
        print(s, ss)
        k+=1
print(k)


