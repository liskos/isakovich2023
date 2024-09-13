import itertools

for s, a in enumerate(itertools.product('АМРТ', repeat=4), 1):
    ss = ''.join(a)
    if s == 250:
        print(ss)
        break
