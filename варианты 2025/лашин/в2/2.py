def f(x, y, z, w):
    return (w == (not(not y or z))) and x



import itertools


for a in itertools.product([0, 1], repeat=6):
    table = [(0, a[0], a[1], a[2]), (0, 0, a[3], a[4]), (0, 0, 0, a[5])]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1] and len(set(table)) == 3:
            print(p)