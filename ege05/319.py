def f(n):
    b = bin(n)[2:]
    if n % 10 == 0:
        b = b + b[-4] + b[-3] + b[-2] + b[-1]
    else:
        b = b + bin(int(b[-1])**2//2)[2:]
    return int(b, 2)

a = []
for i in range(11, 10000):
    if f(i) < 680:
        a.append(i)
print(len(a))