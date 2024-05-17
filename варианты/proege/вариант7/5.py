def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return s


def f(n):
    s = tr(n)
    if n % 3 == 0:
        s += s[-2] + s[-1]
    else:
        s += tr(n % 3 * 5)
    return int(s, 3)


a = []
print(f(11), f(12))
for i in range(1, 10000):
    if f(i) > 133:
        a.append(f(i))
print(min(a))

