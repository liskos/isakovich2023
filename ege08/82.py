import itertools



for s, i in enumerate(itertools.product('АВГДИНОР', repeat=4), 1):
    ss = ''.join(i)
    if 'ИР' in ss[:2]:
        print(s, ss)
        break

