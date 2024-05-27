def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '1'
    else:
        b = b + '0'
    if n % 2 == 0:
        b = b + '1'
    else:
        b = b + '0'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) < 171:
        a.append(i)
print(max(a))