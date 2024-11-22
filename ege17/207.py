def f(a, b):
    return (a % 10 == 7 or b % 10 == 7) and (a + b) % 12 == 0


a = [int(x) for x in open('17data/17-205.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), max(c))