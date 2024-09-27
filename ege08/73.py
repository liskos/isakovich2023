import itertools



for s, i in enumerate(itertools.product('АРТФ', repeat=5), 1):
    ss = ''.join(i)
    if 'Т' in ss[0]:
        print(s, ss)
        break

