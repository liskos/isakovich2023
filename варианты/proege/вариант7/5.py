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
        s += s[:-1] + s[:-2]
    else:
        s += tr(n % 5)
    return int(s, 3)


for i in range(1, 10000):
    if f(i) > 133:
        print(f(i))
        break

