def f(x, y, z, w):
    return not(not y or x) and not(not w and z) and not(x and w)


import itertools


for a in itertools.product([0, 1], repeat=7):
    table = [(a[0], a[1], 0, a[2]), (a[3], a[4], 1, 0), (1, a[5], a[6], 1)]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1] and len(set(table)) == 3:
            print(p)