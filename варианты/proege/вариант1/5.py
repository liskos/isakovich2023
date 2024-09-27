def sh(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 6] + s
        n = n // 6
    return s


def f(n):
    b = sh(n)
    if n % 3 == 0:
        b = b[:2] + b
    if n % 3 == 1:
        sh(n % 3 * 10) + b
    return int(b, 6)


a = []
for i in range(1, 10000):
    if f(i) > 680:
        a.append(f(i))
print(min(a))