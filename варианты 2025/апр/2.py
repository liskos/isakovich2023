def f(x, y ,z, w):
    return (not w or not(not z or x)) or y

import itertools
for a in itertools.product([0, 1], repeat=8):
    table = [(1, a[0], a[1], a[2]), (0, 1, 0, a[3]), (a[4], 0, a[5], a[6])]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(p)
