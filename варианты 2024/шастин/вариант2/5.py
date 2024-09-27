def sem(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n = n // 7
    return s

def f(n):
    s = sem(n)
    if s.count("2") % 2 == 0:
        s = s + "555"
    else:
        s = "1" + s
    return int(s, 7)

a = []
for i in range(1, 10000):
    if f(i) < 3799:
        a.append(i)
print(max(a))