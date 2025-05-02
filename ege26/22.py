def f(filename):
    file = open(filename)
    n, k = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    v = a[k:-k]
    print(f'кол-во измерений {n}, кол-во исключаемых измерений {k}')
    print(f'измерения: {a}')
    print(f'достоверные измерения: {v}')
    return v[-1], sum(v) // len(v)

print(f('26data/26-k2.txt'))