


def f(x,y,z,w):
    return (not(not(not y or x) or w)) or (not z or x)

import itertools
for a in itertools.product([0, 1], repeat=6):
    table = [(a[0], 0, 0, a[1]), (a[2], 1, 1, 0), (a[3], 1, a[4], a[5])]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(p)