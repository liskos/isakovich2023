def f(n):
    b = bin(n)[2:]
    if n % 100 // 10 == b.count('1'):
        return n + 25
    else:
        return n - 25

c=[]
for i in range(100, 201, 2):
    r = f(i)
    if int(str(r)[1])  == bin(r)[2:].count('1'):
        c.append(f(i))
print(len(c))