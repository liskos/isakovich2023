def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b[:3] + b
    else:
        b = b + bin((n%5) * 5)[2:]
    return int(b, 2)

a = []
for i in range(1, 1000):
    if f(i) < 313 and f(i) % 3 == 0:
        a.append(i)
print(max(a))