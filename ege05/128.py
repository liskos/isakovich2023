def f(n):
    s = str(n)
    a1 = int(s[0]) + int(s[1])
    a2 = int(s[1]) + int(s[2])
    a3 = int(s[2]) + int(s[3])
    d = str(a1 + a2 + a3 - min(a1, a2, a3) - max(a1, a2, a3))
    c = str(min(a1, a2, a3))
    return str(d) + str(c)

m = ""
for i in range(1000, 10000):
    if f(i) == "118":
        m = i
print(m)