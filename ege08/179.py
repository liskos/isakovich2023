import itertools


for s, i in enumerate(itertools.product('ЩОГБА', repeat=6), 1):
    ss = ''.join(i)
    if 'ОБЩАГА' in ss:
        print(s, ss)
