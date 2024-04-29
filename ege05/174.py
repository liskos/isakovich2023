def f(n):
    s = bin(n)[2:]
    while s[0] != "1":
        s = s[:-1]
    return int(s, 2)

k = 0
for i in range(10, 2501):
    if f(i) == i:
        k += 1
print(k)