def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i**2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b

pr = prime(2532161)
p = [[i, x] for i, x in enumerate(pr, 1) if 2532001<= x <= 2532160 and x % 10 == 7]
print(*p, sep="\n")

