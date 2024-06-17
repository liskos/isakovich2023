def f(n):
    b = bin(n)[2:]
    if n % 7 == 0:
        b = b + '111'
    else:
        b = b + '1'
    if int(b, 2) % 5 == 0:
        b = b + '101'
    else:
        b = b + '1'
    return int(b, 2)

a = []
for i in range(1, 1000000):
    if f(i) > 500000:
        a.append(i)
print(min(a))