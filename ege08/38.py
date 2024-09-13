import itertools



for s, i in enumerate(itertools.product('АОУ', repeat=5), 1):
    ss = ''.join(i)
    if 'УАУАУ' in ss or 'ОУОУА' in ss:
        print(s, ss)
print(183 - 151 + 1)


