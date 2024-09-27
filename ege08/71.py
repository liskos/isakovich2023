import itertools



for s, i in enumerate(itertools.product('ЕИКНУЧ', repeat=3), 1):
    ss = ''.join(i)
    if 'К' in ss[0]:
        print(s, ss)
        break

