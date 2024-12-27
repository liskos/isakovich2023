def f(x, y, z, w):
    return (not (not y or x) or w) == (z or y or w)

import  itertools
for a in itertools.product([0, 1], repeat=4):
    table = [(0, 1, a[0], 1), (1, 0, a[1], 1), (1, 0, a[2], a[3])]
    for p in itertools.permutations("xyzw"):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0] and len(set(table))==3:
            print("".join(p))