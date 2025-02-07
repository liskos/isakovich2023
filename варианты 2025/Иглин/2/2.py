def f(x, y, z, w):
    return ((not x and not z) or z) or (y and not(y or w))


import itertools

for a in itertools.product([0, 1], repeat=7):
    table = [(1, a[0], 1, a[1]), (1, 0, a[2], a[3]), (a[4], 0, 0, 0)]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 1, 0] and len(set(table)) == 3:
            print(p)