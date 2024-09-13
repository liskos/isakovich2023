import itertools



for s, i in enumerate(itertools.product('АКРУ', repeat=5), 1):
    ss = ''.join(i)
    if 'РУКАА' in ss or 'УКАРА' in ss:
        print(s, ss)
print(841 - 721 + 2)


