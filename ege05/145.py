def f(n):
    b = bin(n)[2:]
    b1 = b + b[-1]
    if b.count("1") % 2 == 0:
        b1 += "0"
    else:
        b1 += "1"
    if b1.count("1") % 2 == 0:
        b1 += "0"
    else:
        b1 += "1"
    return int(b1, 2)


for i in range(1, 100000):
    if f(i) > 80:
        print(f(i))
        break