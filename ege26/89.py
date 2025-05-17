def f(filename):
    k = 3
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    v = []
    v.append(a[0])
    for x in a:
        if v[-1] >= x + k:
            v.append(x)
    return len(v), v[-1]

print(*f('89test.txt'))
print(*f('26data/26-89.txt'))