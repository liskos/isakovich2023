def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + bin(b.count('1'))[2:]
    else:
        b = "1" + b + "00"
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) > 215:
        a.append(i)
print(min(a))