def f(n):
    b = bin(n)[2:]
    if n % 10 == b.count('1'):
        return 1
    else:
        return 0

c=[]
for i in range(100, 201, 2):
    if f(i):
        c.append(f(i))
print(len(c))