def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return s

def f(n):
    b = tr(n)
    if n % 5 == 0:
        b = '10' + b[2:] + '1'
    else:
        b = tr(n % 5) + b
    return int(b, 3)

a = []
for i in range(10, 10000):
    if f(i) < 504:
        a.append(f(i))
print(max(a))