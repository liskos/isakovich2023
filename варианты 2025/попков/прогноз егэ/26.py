from collections import Counter


def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    summa = [x[1] for x in a]
    sr = sum(summa) // len(summa)
    r = []
    stand = []
    lead = []

    for x in a:
        if x[1] >= sr:
            r.append(x)
        else:
            stand.append(x)
    for x in r:
        if x[-1] == 0:
            lead.append(x)
    v2 = []
    for x in r:
        if x[-1] == 1 and x[0] == 93476:
            v2.append(x[0])
    idr = [x[0] for x in lead]
    leader = Counter(idr)
    v = sum([x[1] for x in lead if x[0] == 93476])
    print(f'проданы премиум {lead}')
    print(f'премиум сегмент {r}')
    print(f'счетчик{leader}')
    return v, len(v2)


print(f('26test.txt'))
print(f('26.txt'))