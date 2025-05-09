def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i**2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    r = [x for x in b if x % 10 == 7]
    return sum(r) // len(r)


for i in reversed(range(10000, 750000, 111)):
    if prime(i) % 111 == 0 and prime(i) != 0:
        print(i, prime(i))