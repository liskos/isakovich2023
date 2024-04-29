def f(n):
    s = bin(n)[2:]
    while len(s) < 8:
        s += "0"
    b = s.replace("1", "2").replace("0", "1").replace("2","0")
    return int(b, 2)


for i in range(1, 1000):
    if f(i) == 99:
        print(i)
        break

