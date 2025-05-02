def f(x, y, z, w):
    return (x and not y) or (y == z) or w

import itertools


for a in itertools.product([0, 1], repeat=4):
    table = [(a[0],a[1],1,a[2]), (0,0,0,1), (1, 0, a[3], 1)]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(p)