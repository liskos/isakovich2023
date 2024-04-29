def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "1"
    else:
        b += "0"
    if b.count("1") % 2 == 0:
        b += "1"
    else:
        b += "0"
    return int(b, 2)

a = 0
for i in range(1, 100000):
    if 16 <= f(i) <= 32:
        a += 1
print(a)