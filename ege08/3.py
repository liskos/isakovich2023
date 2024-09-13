import itertools

for s, a in enumerate(itertools.product('АОУ', repeat=5), 1):
    if s == 170:
        print(a)
