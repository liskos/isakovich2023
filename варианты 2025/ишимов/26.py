def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(file.readline().split()) for _ in range(n)]
    sr1 = [int(x[0]) * int(x[1]) for x in a]
    sr = sum(sr1) / len(sr1)
    r = []
    for x in a:
        if int(x[0]) > 1.5 * sr:
            r.append(x)
    v = [int(x[0]) for x in r]
    return min(v)

print(f('26test.txt'))