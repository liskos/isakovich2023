def f(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n , i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b


for i in range(200, 2023):
    print(f(i))
    if min(f(i)) > 10:
        print(i, f(i))
