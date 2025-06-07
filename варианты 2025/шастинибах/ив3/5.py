def f(n):
    b = bin(n)[2:]
    if (b.count('0') + b.count('1')) % 2 == 0:
        b = b[:len(b)//2] + '010' + b[len(b)//2:]
    else:
        b = b + b[-1]
        b = b[:len(b)//2] + '101' + b[len(b)//2:]
    return int(b, 2)
a = []
for i in range(1, 1000):
    if f(i) > 414:
        a.append(f(i))
print(min(a))