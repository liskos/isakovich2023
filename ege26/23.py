def f(filename):
    file = open(filename)
    n, k, m = map(int, file.readline().split())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    k1 = a[-k]
    m1 = a[m]
    return m1, k1

print(f('23.txt'))
print(f('26data/26-k3.txt'))