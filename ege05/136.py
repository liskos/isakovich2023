def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)


a = []
for i in range(1, 100000):
    if 16<= f(i) <=32:
        a.append(f(i))
print(len(range(16, 33)) - len(set(a)))