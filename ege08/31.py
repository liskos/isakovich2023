import itertools


k = 0
for s, i in enumerate(itertools.product('МЕТРО', repeat=4), 1):
    ss = ''.join(i)
    if ss[0] != 'О' and ss[0] != 'Е' and ss[-1] != 'М' and ss[-1] != 'Т' and ss[-1] != 'Р':
        k+=1
        print(ss)
print(k)

