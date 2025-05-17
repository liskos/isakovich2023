def f(filename):
    file = open(filename)
    n, t = map(int, file.readline().split())
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    a = sorted(a)
    v1 = []
    sup = []
    stand = []
    s = True
    for x in a:
        v1.append(x[0])
    r = round(sum(v1)/len(v1))
    print(round(sum(v1)/len(v1)))
    for x in a:
        if s and x[0] >= r and sum(sup) + sum(stand) <= t:
            sup.append(x[1])
            t = t - x[1]
            s = False
        elif not s and x[0] < r and sum(sup) + sum(stand) <= t:
            sup.append(x[0])
            t = t - x[1]
            s = True
    print(sup)
    print(stand)


print(f('68.txt'))
