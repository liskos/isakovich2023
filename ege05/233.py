def f(n):
    b = bin(n)[2:]
    if b.count('1') > b.count('0'):
        b = b + '0'
    else:
        b = b + '1'
    if len(b) % 2 == 0:
        b = b[:len(b)//2 - 1] + b[len(b)//2 + 1:]
    else:
        b = b[:len(b)//2 - 1] + b[len(b)//2 + 2:]
    return int(b, 2)

a = []
for i in range(4, 1000):
    if f(i) == 58:
        a.append(i)
print(len(a))