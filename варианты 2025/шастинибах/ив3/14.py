def f(n):
    a = []
    while n > 0:
        a.append(n % 8)
        n = n // 8
    return a
c = []

for x in range(10000):
    r = 8 ** 200 + 2 ** 100 - 2 * x
    c.append([x, sum(f(r))])

for i in c:
    if i[1] == 3:
        print(i)
