import itertools

for s, a in enumerate(itertools.product('АКРУ', repeat=5), 1):
    if s == 150:
        print(a)
