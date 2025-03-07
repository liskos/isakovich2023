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
pr = prime(473266)
for x in range(412567, 473265):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            y = x // i
            if i in pr and i != y and y in pr:
                a.append(x)
            break
for i in range(len(a)):
    if a[i] == sum(a)//len(a) + i:
        print(a[i])
print(len(a))