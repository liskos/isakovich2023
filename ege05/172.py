def f(n):
    s = bin(n)[2:]
    while len(s) < 8:
        s = "0" + s
    b = s[0] + s[1] + s[-2] + s[-1]
    return int(b, 2)

k = 0
for i in range(1, 110):
    if f(i) == 7:
        print(i)
print(k)