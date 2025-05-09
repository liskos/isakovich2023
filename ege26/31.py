def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    print(f'{n} товаров')
    print(a)
    v = [x for x in a if x > 100]
    v = sorted(v)
    print(f'больше 100 рублей {v}')
    k = len(v) // 2
    print(f"{k} кол-во со скидкой")
    t = v[:k]
    print(f"товары со скидкой {t}")
    sk = int(sum(t) * 0.1)
    print(sum(t) - sk)

    return sum(a) - sk, t[-1]

print(*f('31.txt'))
print(*f('26data/26-s1.txt'))