def f(a, b):
    return a % 9 == 0 and int(oct(b)[3:], 8) % 10 == 3


a = [int(x) for x in open('17data/17-1.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        c.append(a[i])
        c.append(a[i+1])
print(len(c), max(c))