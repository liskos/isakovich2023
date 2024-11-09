def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = '1' + b[:-2] + '11'
    else:
        b = '10' + b + '0'
    return int(b, 2)

a = []
for i in range(1, 1000, 2):
    if f(i) > 999:
        a.append(f(i))
print(min(a))