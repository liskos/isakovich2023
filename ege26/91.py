def f(filename):
    file = open(filename)
    n, d = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    v = []
    nv = []
    for i in range(len(a) - 1):
        if a[i] + a[i+1] <= d:
            v.append([a[i], a[i+1]])
        else:
            nv.append(a[i])
    print(f'подходящие {v}')
    print(f'больше D {nv}')
    return len(v), sum(nv)


print(f('91test.txt'))