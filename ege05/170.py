def f(n):
    s = bin(n)[2:]
    b = s[::-1]
    while b[0] == "0":
        b = b[1:]
    return int(b, 2)


for i in range(1000, 10000):
    if f(i) == 29:
        print(i)
        break