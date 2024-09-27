import itertools



for s, i in enumerate(itertools.product('АДР', repeat=6), 1):
    ss = ''.join(i)
    if 'Р' in ss[0]:
        print(s, ss)
        break

