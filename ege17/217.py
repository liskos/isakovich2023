def f(a, b):
    return (a < sr or b < sr) and (abs(a) % 100 == 13 or abs(b) % 100 == 13)


a = [int(x) for x in open('17data/17-1.txt')]
sr = sum(a) // len(a)
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), max(c))