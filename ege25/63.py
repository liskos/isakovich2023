def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i**2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b

pr = prime(1532161)
p = [[i, x] for i, x in enumerate(pr, 1) if 2532001<= x <= 2532161]
print(*p, sep="\n")

