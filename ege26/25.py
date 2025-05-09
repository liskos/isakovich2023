def f(filename):
    file = open(filename)
    n, k, m = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    b = a[:k]
    r = a[m:]
    return r[m+4], sum(b) // len(b)


print(*f('25.txt'))
print(*f('26data/26-k5.txt'))