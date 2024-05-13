def f(n):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[:-1] + s[:-2] + s[:-3]
    else:
        s = s + bin(n % 3 * 3)[2:]
    return int(s, 2)


for i in range(1, 10000):
    if f(i) > 151:
        print(f(i))
        break