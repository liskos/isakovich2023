def f(n):
    s = str(n)
    a1 = int(s[0])+int(s[1])
    a2 = int(s[1]) + int(s[2])
    a3 = int(s[2]) + int(s[3])
    d = str(a1 + a2 + a3 - min(a1, a2, a3) - max(a1,a2,a3))
    c = str(max(a1,a2,a3))
    if int(c) > int(d):
        c, d = d, c
    return str(d) + str(c)


for i in range(1000, 10000):
    if f(i) == "126":
        print(i)
        break