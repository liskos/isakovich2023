def f(filename):
    file = open(filename)
    n, k, m = map(int, file.readline().split())
    print(f"всего смартофонов {n}, {k} бюджетные, {m} премиальные")
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    print(a)
    b = a[-k:]
    p = a[:m]
    return p[-1], sum(b) // len(b)


print(*f('25.txt'))
print(*f('26data/26-k5.txt'))