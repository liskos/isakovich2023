def f(x,y,z,w):
    return not(not x or y) or (z == w) or z


import itertools



for a in itertools.product([0, 1], repeat=7):
    table = [(0, 0, a[0], a[1]), (a[2], a[3], 1, a[4]), (a[5], 1, 0, a[6])]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(p)