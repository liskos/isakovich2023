def f(a, b):
    return a % 10 == 6 and b % 3 == 0


a = [int(x) for x in open('17data/17-1.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        c.append(a[i])
        c.append(a[i+1])
print(len(c), min(c))