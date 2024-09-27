import itertools



for s, i in enumerate(itertools.product('АКЛОШ', repeat=4), 1):
    ss = ''.join(i)
    if 'О' in ss[0]:
        print(s, ss)
        break

