from collections import Counter

def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    v = []
    for x in a:
        if x[1] % 2 == 0:
            v.append(x)
    print(f"подходящие точки {v}")
    id = [x[0] for x in v]
    count = Counter(id)
    print(*count)
    v2 = []
    for x in v:
        if x[0] == 3564:
            v2.append(x)
    return len(v2), 3564




print(*f('82test.txt'))
print(*f('26data/26-82.txt'))