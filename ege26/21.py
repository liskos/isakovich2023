def f(filename):
    file = open(filename)
    n, k = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    print(f'кол-во товаров {n}, со скидкой {k}')
    print(f'товары: {a}')
    return a[k], sum(a[:k]) * 0.2


print(f('26data/26-k1.txt'))