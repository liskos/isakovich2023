def f(filename):
    file = open(filename)
    n, s = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    v = []
    k = 0
    for x in a:
        if x + sum(v) <= s:
            v.append(x)
            a.remove(x)
        else:
            v = []
            k += 1
    return k, sum(v)

print(*f('55.txt'))
