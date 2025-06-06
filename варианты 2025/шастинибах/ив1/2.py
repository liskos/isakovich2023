def f(x, y, z, w):
    return ((not z or x) and (not x or y)) or (w == (z or x))


import itertools


for a in itertools.product([0, 1], repeat=7):
    table = [(a[0], 1, a[1], a[2]), (a[3], a[4], 1, 1), (a[5], 1, a[6], 1)]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(p)