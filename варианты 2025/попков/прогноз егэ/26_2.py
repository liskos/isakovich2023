def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = dict()
    for _ in range(n):
        id, cena, stat = map(int, file.readline().split())
         # продано/ не продано
        a[id] = a.get(id, [cena, 0, 0])
        if stat == 1:
            a[id] = [cena, a[id][1],a[id][2]+1]
        else:
            a[id] = [cena, a[id][1] + 1, a[id][2]]
    print(a)
    summa = [a[x][0] * (a[x][1] + a[x][2]) for x in a ]
    col = sum([a[x][1] + a[x][2] for x in a])
    sr = sum(summa) // col
    b = [[x, a[x][0], a[x][1], a[x][2]] for x in a if a[x][0] >= sr]

    b.sort(key=lambda x:(x[2], x[1],-x[3]), reverse=True)
    print(b[0][1] * b[0][2])
    print(b[0][3])


print(f('26test.txt'))
print(f('26.txt'))