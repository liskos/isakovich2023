def ch(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n = n // 4
    return s

def f(n):
    b = ch(n)
    b = str(n % 2) + b + str(n % 3)
    return int(b, 4)


a = []
for i in range(1, 10000):
    if 9 < f(i) < 100:
        a.append(f(i))
print(max(a))