import itertools


def f(x, y, z, w):
    return not(x == (not y)) or ((x or z) == w)


for a in itertools.product([0, 1],repeat=5):
    table = [(0,a[0],a[1],0),(0,a[2],0,a[3]),(0,0,a[4],0)]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
            print("".join(p))

