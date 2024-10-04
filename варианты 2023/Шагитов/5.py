def tr(n):
    s = ""
    t = "012"
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return s


def f(n):
    b = tr(n)
    if n % 3 == 0:
        b = '1' + b + '02'
    else:
        b = b + tr(n % 3 * 4)
    return int(b, 3)

print(f(11))
a = []
for i in range(1, 10000):
    if f(i) < 199:
        a.append(i)
print(max(a))