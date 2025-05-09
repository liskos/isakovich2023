def f(filename):
    file = open(filename)
    n, k, m = map(int, file.readline().split())
    print(f"всего участников {n}, {k} победителей, {m} призеров")
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a, reverse=True)
    print(a)
    k1 = a[k-1]
    m1 = a[m+k-1]
    return m1, k1

print(f('23.txt'))
print(f('26data/26-k3.txt'))