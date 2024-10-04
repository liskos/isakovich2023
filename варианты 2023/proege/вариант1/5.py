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
        b = b + b[:2]
    if n % 3 >= 1:
        b = b + sh(n % 3 * 10)
    return int(b, 6)

print(f(11),f(12))
a = []
for i in range(1, 10000):
    if f(i) > 680:
        a.append(f(i))
print(min(a))