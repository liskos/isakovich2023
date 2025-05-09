def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    v = []
    for x in a:
        if x > 100 and len(v) % 2 == 0:
            v.append(x + x * 0.1)
        elif x > 100:
            v.append(x)
    return sum(v), max(v) - max(v) * 0.1

print(*f('31.txt'))