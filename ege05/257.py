def f(n):
    b = bin(n)[2:]
    b = b + str(b.count("1") % 2)
    if b.count("1") > b.count("0"):
        b = b + "0"
    else:
        b = b + "1"
    return int(b, 2)


for i in range(1, 10000):
    if f(i) > 80:
        print(f(i))
        break