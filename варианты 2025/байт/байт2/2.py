def f(x, y, z, w):
    return x or ((not y or w) and ((y or z) or not w))


import itertools


for a in itertools.product([0, 1], repeat=6):
    table = [(1, a[0], a[1], a[2]), (0, 1, a[3], 0), (a[4], 1, a[5], 1)]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(p)