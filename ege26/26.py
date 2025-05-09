def f(filename):
    k = 0
    file = open(filename)
    n = int(file.readline())
    a = [0] * 100
    print(a)
    for _ in range(n):
        a[int(file.readline())] += 1
    print(a)
    for i in range(1, 50):
        k += min(a[i], a[-i])
    k += a[50] // 2
    print(k)


print(f('26.txt'))
print(f('26data/26-J1.txt'))
