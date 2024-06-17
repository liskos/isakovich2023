def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = '1' + b + b[-2] + b[-1]
    else:
        b = bin(n % 5)[2:] + b
    return int(b, 2)

a = []
for i in range(1, 1000):
    if f(i) <= 223:
        a.append(i)
print(max(a))