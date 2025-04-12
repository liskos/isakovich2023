def f(x, y, z, w):
    return x and (not z or w) and not y


import itertools


for a in itertools.product([0, 1], repeat=7):
    table = [(a[0], a[1], 1, a[2]), (a[3], 1, 0, a[4]), (1, 0, a[5], a[6])]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1] and len(set(table)) == 3:
            print(p)