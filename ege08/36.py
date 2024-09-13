import itertools



for s, i in enumerate(itertools.product('АМРТ', repeat=4), 1):
    ss = ''.join(i)
    if 'МАРТ' in ss or 'РАМТ' in ss:
        print(s, ss)
print(136 - 76 + 1)


