def f(filename):
    c = 6
    file = open(filename)
    n, k = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    b = a[:c]
    v = []
    skidka = [int(x * 0.5) for x in b]
    print(f'товары, которые получат скидку {b}')
    print(f'получили скидку {skidka}')
    skidka += a[c:]
    skidka = sorted(skidka)
    for x in skidka:
        if sum(v) + x <= k:
            v.append(x)
    print(len(v), k - sum(v))




print(f('105.txt'))
print(f('26data/26-105.txt'))