def f(x, y, z, w):
    return (not z or y) or (not(not w or x) or y)

import itertools


for a in itertools.product([0, 1], repeat=6):
    table = [(a[0], 0, 0, a[1]), (a[2], a[3], 1, a[4]), (a[5], 1, 1, 1)]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(*p)