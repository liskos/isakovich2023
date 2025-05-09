def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i**2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    r = [x for x in b if x % 10 == 7]
    return r
def f(n):
    global p7
    r = [x for x in p7 if n % x == 0 and x < n]
    if r:
        return sum(r) // len(r)
    return 0
p7 = prime(750000)
z = 0
for i in reversed(range(10000, 750000)):
    k = f(i)
    if k % 111 == 0 and k != 0:
        z += 1
        print(i, k)
        if z == 5:
            break