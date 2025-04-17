def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i**2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b


def q(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sum(a)
k = 0
for i in range(1000000, 10 ** 10):
    if len(prime(q(i))) > 1:
        print(i, q(i))
        k += 1
    if k == 5:
        break