import itertools

for s, a in enumerate(itertools.product('АОУ', repeat=5), 1):
    if s == 101:
        print(a)