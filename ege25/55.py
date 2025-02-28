def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i**2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b

pr = prime(5336835)
p = [[i, x] for i, x in enumerate(pr, 1) if 5336748<= x <= 5336834]
print(*p, sep="\n")

