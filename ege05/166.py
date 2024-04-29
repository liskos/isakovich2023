def f(n):
    s = bin(n)[2:]
    b = s[::-1]
    while b[0] == "0":
        b = b[1:]
    return int(b, 2)


for i in range(100, 10000):
    if f(i) == 7:
        print(i)
        break