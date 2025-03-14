def f(x, y, z, w):
    return x and ((not w or y) == z)


import itertools


for a in itertools.product([0, 1], repeat=5):
    table = [(a[0], a[1], 0, 0), (0, a[2], a[3], 0), (a[4], 1, 1, 1)]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 0] and len(set(table)) == 3:
            print(p)