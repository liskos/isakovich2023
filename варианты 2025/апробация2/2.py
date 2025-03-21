import itertools


def f(x, y, z, w):
    return not(not x or y) or (not z or w) or not z

for a in itertools.product([0, 1], repeat=7):
    table = [(a[0], 0, a[1], 0), (1, a[2], a[3], a[4]), (0, 1, a[5], a[6])]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(p)