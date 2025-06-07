def f(n):
    if n < 3000:
        return n
    if n >= 3000 and n % 7 == 0:
        return n + f(n//7)
    return 29 + f(n - 3)
for i in range(100000):
    if f(i) > 100000:
        print(i)
        break