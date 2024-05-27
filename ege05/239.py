def sh(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return int(s, 6)


def f(n):
    s = bin(sh(n))[2:]
    s = s + s[-1]
    return int(s, 2)

a = []
for i in range(1, 10000):
    if f(i) < 344:
        a.append(f(i))
print(max(a))