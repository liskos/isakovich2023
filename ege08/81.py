import itertools



for s, i in enumerate(itertools.product('АВГДИНОР', repeat=4), 1):
    ss = ''.join(i)
    if 'ГО' in ss[:2]:
        print(s, ss)
        break

