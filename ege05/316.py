def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b + b[-3] + b[-2] + b[-1]
    else:
        b = b + bin(n % 5 * 5)[2:]
    return int(b, 2)

a = []
for i in range(4, 10000):
    if f(i) < 100:
        a.append(i)
print(max(a))