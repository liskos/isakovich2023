def f(filename):
    file = open(filename)
    n, m = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    v = []
    for x in a:
        if x + sum(v) <= m and x <= 200:
            v.append(x)
    return len(v), sum(v)

print(*f('39.txt'))
print(*f('26data/26-39.txt'))
