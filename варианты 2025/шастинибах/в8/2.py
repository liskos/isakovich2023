import itertools

def f(x, y, z, w):
    return (not z or x) and (not(x and (y != z)) or w)



for a in itertools.product([0, 1], repeat=5):
    table = [(a[0], 1, 1, a[1]), (0, 0, a[2], a[3]), (a[4], 0, 0, 0)]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table)) == 3:
            print(p)