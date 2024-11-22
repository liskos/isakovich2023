def f(a, b):
    return (a + b) % 3 == 0 and (a + b) % 6 > 0 and (a * b) % 10 == 8


a = [int(x) for x in open('17data/17-3.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), max(c))