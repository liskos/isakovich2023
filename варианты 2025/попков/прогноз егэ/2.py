def f(x, y, z, w):
    return not z and not(y and not x) and not(x == w)


import itertools


for a in itertools.product([0, 1], repeat=4):
    table = [(0, 1, 0, 0), (a[0], 1, 0, 1), (1, a[1], a[2], a[3])]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1] and len(set(table)) == 3:
            print(p)