def f(n):
    s = bin(n)[2:]
    while len(s) < 8:
        s += "0"
    b = s[0] + s[1] + s[-2] + s[-1]
    return int(b, 2)


for i in range(131, 10000):
    if f(i) == 10:
        print(i)
        break