def f(n):
    if n < 15:
        return 4
    if n >= 15 and n % 3 == 0:
        return f(2 * n/3) + n - 1
    if n >= 15 and n % 3 != 0:
        return f(n-1) + 3
c = []
for i in range(1, 1000):
    if f(i) == 251:
        c.append(i)
print(max(c))