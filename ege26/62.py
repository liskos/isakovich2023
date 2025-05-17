def f(filename):
    file = open(filename)
    n, m = map(int, file.readline().split())
    a = [list(file.readline().split()) for _ in range(n)]
    a = [[int(x[0]), x[1]] for x in a]
    a = sorted(a)
    print(a)
    v = []
    s = 0
    for x in a.copy():
        if int(x[0]) <= m - s:
            v.append(x)
            s += x[0]
            a.remove(x)
        else:
            break
    print("выбранные", v)
    print(f"выбрано товаров {len(v)}")
    a = [x for x in a if x[1] != 'Z']
    print("остались", a)
    print("осталось денег", m - s)
    v.reverse()
    for i in range(len(v)):
         if v[i][1] == 'Z' and m - s + v[i][0] >= a[0][0]:
            s -= v[i][0]
            s += a[0][0]
            v[i] = a.pop(0)
    print("остались", a)
    print("выбранные", v)
    print("осталось денег",m - s)
    q = len([x for x in v if x[1] == 'Q'])
    return q




#print(f('62.txt'))
print((f('26data/26-62.txt')))