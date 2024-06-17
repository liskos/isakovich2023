def f(n):
    b = bin(n)
    s = n - b.count('0')
    s = bin(s)[2:]
    s = s[-3:] + s
    return int(s, 2)

a = []
for i in range(1, 10000):
    if f(i) > 224:
        a.append(f(i))
print(min(a))