def f(n):
    s = bin(n)[2:]
    while len(s) < 8:
        s = "0" + s
    b = s[:-1]
    b = b[::-1]
    return int(b, 2)

k = 0
for i in range(1, 100):
    if f(i) == i:
        k = i
print(k)