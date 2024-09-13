import itertools

for s, a in enumerate(itertools.product('АКРУ', repeat=5), 1):
    ss = ''.join(a)
    if ss == 'РУКАА':
        print(s, ss)
        break
