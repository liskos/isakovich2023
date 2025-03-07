def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b

pr = prime(51238)
p = [x for x in pr if 25317 <= x <= 51237]
print(p)