def f(n):
    s = bin(n)[2:]
    s = s + s[-2] + s[1]
    return int(s, 2)

a = []
for i in range(3, 10000):
    if 150 <= f(i) <= 250:
        a.append(i)
print(len(a))
