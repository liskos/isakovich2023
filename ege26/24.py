def f(filename):
    file = open(filename)
    n, k = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    k5 = sum(a[:k]) // len(a[:k])
    k4 = sum(a[k:k+k]) // len(a[k:k+k])
    return k4, k5

print(*f('24.txt'))
print(*f('26data/26-k4.txt'))