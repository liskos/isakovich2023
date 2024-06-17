def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) > 2023:
        a.append(i)
print(min(a))