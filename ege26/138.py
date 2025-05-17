def f(filename):
    file = open(filename)
    n = int(file.readline())
    k = int(file.readline())
    m = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    v = []
    for x in a:
        if sum(v) + x <= m:
            v.append(x)
            a.remove(x)

    print(v)
    print(a)
    print(k)

print(f('138.txt'))