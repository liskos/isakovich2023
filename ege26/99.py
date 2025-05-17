def f(filename):
    file = open(filename)
    n, m = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    v = []
    n1 = 0
    for x in a:
        if sum(v) + x <= m:
            v.append(x)
        else:
            n1 = sum(v)
            v = []
    print(n1)


print(f('99.txt'))
