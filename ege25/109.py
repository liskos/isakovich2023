def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b

a = []
pr = prime(217438)
for x in range(173225, 217437):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            y = x // i
            if i in pr and i != y and y in pr and y % 10 == i % 10:
                a.append(x)
            break
print(len(a), min(a))