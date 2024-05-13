def f(n):
    s = bin(n)[2:]
    s = s + str(s.count("1") % 2)
    s = s + str(s.count("1") % 2)
    return int(s, 2)

a = []
for i in range(1, 10000):
    if 210 <= f(i) <= 260:
        a.append(i)
print(len(a))
