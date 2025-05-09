def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    v = []
    for i in range(len(a) - 1):
        if (a[i] + a[i+1]) % 3 == 0 and (a[i] + a[i+1]) // 2 in a:
            v.append(a[i]+a[i+1] // 2)
    return len(v), min(v)

print(*f('46.txt'))