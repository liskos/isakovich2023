def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i**2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b
k = 0
for i in range(10000, 10**10, 7):
    if len(prime(i)) == 4 and i % 7 == 0:
        print(i, max(prime(i)))
        k += 1
        if k == 7:
            break