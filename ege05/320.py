def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return s

def f(n):
    b = tr(n)
    if n % 2 == 0:
        b = b + b[0] + b[1]
    else:
        b = b + tr(b.count('1') + b.count('2') * 2)
    return int(b, 3)

a = []
for i in range(3, 10000):
    if f(i) < 100:
        a.append(i)
print(min(a))