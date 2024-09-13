import itertools

for s, a in enumerate(itertools.product('АМРТ', repeat=5), 1):
    ss = ''.join(a)
    if s == 250:
        print(ss)
        break
