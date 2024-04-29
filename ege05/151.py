def f(n):
    b = bin(n)[2:]
    b += b[-1]
    if b.count("1") % 2 == 0:
        b += "01"
    else:
        b += "10"
    return int(b, 2)


for i in range(1, 100000):
    if f(i) > 62:
        print(i)
        break