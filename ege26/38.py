def f(filename):
    file = open(filename)
    s, n = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    v = []
    while sum(v) <= 100:
        v.append(max(a))
        a.remove(max(a))
        v.append(min(a))
        a.remove(min(a))
    print(v)
    return len(v), v[-1]

print(*f('38.txt'))
