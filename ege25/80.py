def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b

p = prime(10000000)
print("про")
m = 0
for i in range(2, 10000001):
    x = [j for j in p if i % j == 0]
    m = max(m, len(x))
print(m, "max")
for i in range(2, 10000001):
    x = [j for j in p if i % j == 0]
    if len(x) == m:
        print(i, len(x))
        break


