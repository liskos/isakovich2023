import itertools



for s, i in enumerate(itertools.product('АОУ', repeat=5), 1):
    ss = ''.join(i)
    if 'У' in ss[2]:
        print(s, ss)
        break



