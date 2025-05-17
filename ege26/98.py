def f(filename):
    file = open(filename)
    n, s = map(int, file.readline().split())
    a = [file.readline().split() for _ in range(n)]
    a = sorted(a)
    print(f'товары без учета скидки {a}')
    v1 = []
    for x in a:
        if x[1] == 'BC':
            v1.append([int(int(x[0]) / 1.2), x[1]])
        elif x[1] == 'AC':
            v1.append([int(int(x[0]) / 1.1), x[1]])
        else:
            v1.append([int(x[0]), x[1]])
    v1 = sorted(v1)
    print(f'товары после скидки {v1}')
    v = []
    for x in v1:
        if x[0] + sum(v) <= s:
            v.append(x[0])
    return sum(v)



print(f('98test.txt'))
