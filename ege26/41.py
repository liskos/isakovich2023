def f(filename):
    file = open(filename)
    d, e, n = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    d1 = []
    e1 = []
    for x in a:
        if x > 500 and sum(d1) + x <= d:
            d1.append(x)
        elif x <= 500 and sum(e1) + x <= e:
            e1.append(x)
    return len(d1) + len(e1), max(d1) + max(e1)

print(*f('41.txt'))
print(*f('26data/26-j10.txt'))