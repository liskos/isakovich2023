def f(n):
    if n == 0:
        return 0
    if n > 0:
        return 3 * n + f(n-1)

for i in range(1, 10000):
    if f(i) > 17505:
        print(i)
        break