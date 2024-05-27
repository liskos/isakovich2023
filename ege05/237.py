def f(n):
    b = bin(n)[2:]
    if n % 2 == 1:
        b = b + '0'
    else:
        b = '1' + b
    if b.count('1') % 2 == 0:
        b = b + '1'
    else:
        b = b + '0'
    return int(b, 2)


for i in range(1, 1000):
    if f(i) > 228:
        print(i)
        break