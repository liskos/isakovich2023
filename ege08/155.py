import itertools


for s, i in enumerate(itertools.product('АИОУЭ', repeat=6), 1):
    ss = ''.join(i)
    if ss[0] == 'О' and ss[-1] == 'О':
        print(s, ss)

