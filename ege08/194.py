import itertools


for x in range(3, 10):
    a = set()
    print(x, end=' ')
    for i in itertools.product('ЛИДА', repeat=x):
        ss = ''.join(i)
        if ss.count('А') <= 2 and ss.count('И') <= 2 and 'Л' not in ss[1:] and 'Д' not in ss[1:]:
            a.add(ss)
    print(len(a))
