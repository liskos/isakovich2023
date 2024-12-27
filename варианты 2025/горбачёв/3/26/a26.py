from audioop import reverse


def f(filename):
    file = open(filename)
    n, s = map(int, file.readline().split())
    print(n, s)
    condidats = []
    with file:
        for line in file:
            id, e1, e2, e3, sob = map(int, line.split())
            condidats.append([id, e1 + e2 + e3, sob])
    print(condidats)
    cond = dict()
    for i, e123, sob in condidats:
        cond[e123] = cond.get(e123, []) + [[i, e123, sob]]
    print(cond)
    k = 0
    polu = 0
    for summa in sorted(cond.keys(), reverse=True):
        k += len(cond[summa])
        if k >= s:
            polu = summa
            break
    print(polu)

    x = sorted(cond[polu], key=lambda x:x[2], reverse=True)
    print(k, s)
    print(x)
    return 0, k - s


if __name__ == '__main__':
    print(f('26.txt'))