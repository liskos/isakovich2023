def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '10'
    else:
        b = '1' + b + '01'
    return int(b, 2)

a = []
for i in range(1, 10000):
    if f(i) > 420:
        a.append(i)
print(min(a))