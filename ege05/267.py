def f(n):
    b = bin(n)[2:]
    b = b[0] + b[1:].replace('0', '2').replace('1', '0').replace('2','1')
    b = int(b, 2)
    return b + n

a = []
for i in range(1, 10000):
    if f(i) > 99 and f(i) % 2 == 1:
        a.append(i)
print(min(a))