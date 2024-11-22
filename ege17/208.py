def f(a, b):
    return (abs(a) % 100 == 17 or abs(b) % 100 == 17) and (a + b) % 2 == 0


a = [int(x) for x in open('17data/17-205.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), max(c))