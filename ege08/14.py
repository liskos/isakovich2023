import itertools

for s, a in enumerate(itertools.product('АКРУ', repeat=5), 1):
    ss = ''.join(a)
    if ss[0] == 'К':
        print(s, ss)
        break
