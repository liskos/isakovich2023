def f(filename):
    file = open(filename)
    n, m = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    v = []
    for x in a:
        if x + sum(v) < m // 2:
            v.append(x)
        else:
            break
    a = sorted(a, reverse=True)
    for x in a:
        if sum(v) + x <= m:
            v.append(x)
    return len(v), max(v)

print(*f('61.txt'))