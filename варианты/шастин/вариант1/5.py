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
        s += s[:2]
    else:
       s = s + tr(n % 3 * 5)
    return int(s, 3)

a = []
for i in range(1, 10000):
    if f(i) > 64:
        a.append(f(i))
print(min(a))
