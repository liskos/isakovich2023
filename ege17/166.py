def f(a, b, c):
    return a < b < c


a = [int(x) for x in open('17data/17-3.txt')]
c = []
for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        c.append(max(a[i], a[i+1], a[i+2] - min(a[i], a[i+1], a[i+2])))
print(len(c), min(c))