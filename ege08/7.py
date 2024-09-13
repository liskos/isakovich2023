import itertools

for s, a in enumerate(itertools.product('АКРУ', repeat=5), 1):
    if s == 350:
        print(a)
