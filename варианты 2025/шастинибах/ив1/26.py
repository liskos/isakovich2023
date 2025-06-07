def min_t(t):
    t.sort()
    m = 10**10
    for i in range(len(t)-1):
        m = min(m, t[i+1] - t[i])
    return m


def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    a.sort(key=lambda x:(x[0], x[1]))
    print(a[:10])
    b = [[0, 0, []]]
    for x, y, t in a:
        if (x == b[-1][0]) and (y == b[-1][1]):
            b[-1][2].append(t)
        else:
            b.append([x, y, [t]])
    print(b[:10])
    c = []
    for x, y, t in b:
        if len(t) >= 2:
            c.append([x, y, min_t(t)])
    print(c[:10])
    c.sort(key=lambda x:x[2])
    print(c[:10])


print(f('26.txt'))