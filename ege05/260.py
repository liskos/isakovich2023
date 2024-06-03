def f(n):
    b = bin(n)[2:]
    if b[-1] == "0":
        b = b[:-1] + b[0] + b[1]
    else:
        pass
    b = b[::-1]
    return int(b, 2)

a = []
for i in range(2, 10000):
    if f(i) == 123:
        a.append(f(i))
print(min(a))