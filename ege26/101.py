def f(filename):
    file = open(filename)
    n, k = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    v = []
    v.append(a[0])
    v1 = []
    for x in a:
        if v[-1] >= x + k:
            v.append(x)
        else:
            v1.append(x)
    return len(v), len(v1) + len(v)

print(*f('101.txt'))
print(*f('26data/26-101.txt'))