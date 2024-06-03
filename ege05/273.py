def f(n):
    b = bin(n)[2:]
    if n % 2 == 1:
        b = '1' + b + '0'
    else:
        b = '11' + b + '11'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) < 126:
        a.append(i)
print(max(a))