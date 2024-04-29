def f(n):
    b = bin(n)[2:]
    b += b[-1]
    if bin(n).count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)


for i in range(1, 100000):
    if f(i) > 105:
        print(f(i))
        break