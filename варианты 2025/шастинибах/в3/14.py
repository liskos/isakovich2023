def f(n):
    a = []
    while n > 0:
        a.append(n % 5)
        n //= 5
    return a

c = []
for x in range(1, 5556):
    s = f(5 ** 150 + 5 ** 135 - x)
    if s.count(4) == 134:
        c.append(x)
print(max(c))
