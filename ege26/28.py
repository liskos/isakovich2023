def f(filename):
    file = open(filename)
    s, n = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    v = []
    for x in a:
        if x + sum(v) <= s:
            v.append(x)

    return len(v), min(v)

print(*f('28.txt'))
print(*f('26data/26-J3.txt'))