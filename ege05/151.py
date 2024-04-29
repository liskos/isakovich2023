def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += "01"
    else:
        b += "10"
    return int(b, 2)

a=[]
for i in range(1, 100000):
    if f(i) > 62:
        a.append(f(i))
print(min(a))