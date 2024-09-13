import itertools

for s, a in enumerate(itertools.product('АОУ', repeat=5), 1):
    ss = ''.join(a)
    if ss[0] == 'У':
        print(ss)
        break
