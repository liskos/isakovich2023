def f(a, b):
    return (a % 2 == 0 and a % 4 == 0) and (b % 2 > 0 and b % 11 == 0)


a = [int(x) for x in open('17data/17-3.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        c.append(a[i] + a[i+1])
print(len(c), max(c))