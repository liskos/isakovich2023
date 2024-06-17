def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + '011'
    else:
        b = b + '1'
    if int(b, 2) % 5 == 0:
        b = b + '101'
    else:
        b = b + '1'
    return int(b, 2)

a = []
for i in range(1, 10000000):
    if f(i) < 10**6:
        a.append(i)
print(max(a))