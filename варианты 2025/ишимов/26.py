def f(filename):
    file = open(filename)
    n = int(file.readline())
    print(f'{n} кол-во видов товаров')
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    print('товары', a)
    sr1 = [x[0] * x[1] for x in a]
    sr = sum(sr1) / sum(x[1] for x in a)
    print('средняя цена', sr)
    r = [x for x in a if x[0] > 1.5 * sr]
    print('дорогие товары', r)
    m = min(r, key=lambda x:(x[0],-x[1]))
    print(m)
    d = sum([x[1] for x in r if x[0] == m[0]])
    return m[1] * m[0], d
print(*f('26.txt'))
print(*f('26test.txt'))