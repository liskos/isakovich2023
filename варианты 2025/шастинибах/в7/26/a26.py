def f(filename):
    file = open(filename)
    n, s = map(int, file.readline().split()) # n - кол во мест в гард,  s  - человек
    print(n, s)
    l = []
    with file:
        for line in file:
            id, t, k = map(int, line.split())
            l.append([id, t, k])
    l = sorted(l, key=lambda x: (x[1], x[0]))
    print(l)
    sdani = []
    ushli = []
    count_number = n
    summa = 0
    a = []
    for id, t, k in l:
        if (id not in sdani) and (id not in ushli):
            if count_number >= k:
                sdani.append(id)
                count_number -= k
                if count_number == 0:
                    a.append([t])
            else:
                ushli.append(id)
                summa += k
        elif (id in sdani) and (id not in ushli):
            count_number += k
            if a and len(a[-1])==1:
                a[-1].append(t)
    print(a)
    return k, 0



if __name__ == '__main__':
    print(f('26.txt'))