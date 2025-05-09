def f(filename):
    k = 0
    file = open(filename)
    k = int(file.readline())
    a = [int(file.readline()) for _ in range(k)]
    a = sorted(a, reverse=True)
    for i in range(len(a) - 1):
        if a[i] + a[i+1] == 100:
            k += 1
    return k


print(f('26.txt'))
