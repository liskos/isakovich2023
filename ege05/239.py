def sh(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 6] + s
        n = n // 6
    return s


def f(n):
    s = sh(n)
    s = s + s[-1]
    s = bin(int(s, 6))[2:]
    s = s + s[-1]
    return int(s, 2)


print(f(13))
a = []
for i in range(1, 10000):
    if f(i) < 344:
        a.append(f(i))
print(max(a))