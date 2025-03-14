def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b


def fac(n):
    b = 1
    for i in range(1, n + 1):
        b = b * i
    return b

p = [2, 3, 5, 7, 11, 13]
for i in reversed(range(1, 15)):
    k = 0
    d = fac(i)
    for j in p:
        if d % j == 0:
            k += 1
    if k % 2 > 0:
        print(i, k)