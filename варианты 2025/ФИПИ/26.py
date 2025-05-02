def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    print(f'число коробок {n}')
    print(f'коробки: {a}')
    v = [a[0]]
    for x in a[1:]:
        if x <= v[-1] - 9:
            v.append(x)
    print(f'выбранные коробки: {v}')
    return len(v), v[-1]


print(*f('26_21910.txt'))