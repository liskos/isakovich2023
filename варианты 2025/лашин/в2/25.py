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
p = prime(100000)
for i in range(10003, 10**10, 7):
    b = [x for x in p if i % x == 0]
    if len(b) == 4:
        print(i, max(b))
        k += 1
        if k == 7:
            break