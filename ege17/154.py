def f(a, b, c):
    return a < b > c


a = [int(x) for x in open('17data/17-1.txt')]
c = []
d = []
for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        c.append(a[i+1])
        d.append(i)
print(len(c), min(d))