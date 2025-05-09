def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    v = []
    for x in a:
        if len(v) % 4 == 0:
            v.append(int(x * 0.5))
        else:
            v.append(x)
    return sum(v)


print(f('90.txt'))
