import itertools

for s, a in enumerate(itertools.product('АОУ', repeat=5), 1):
    ss = ''.join(a)
    if ss == 'ОАОАО':
        print(s)
        break