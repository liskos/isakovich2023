def che(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n = n // 4
    return s


def f(n):
    b = che(n)
    if n % 2 == 1:
        b = '2' + b + '11'
    else:
        b = '13' + b + '02'
    return int(b, 4)

a = []
for i in range(1, 10000):
    if f(i) > 1000:
        a.append(f(i))
print(min(a))