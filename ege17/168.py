def f(a, b, c, d):
    return a > b > c > d and max(a, b, c, d) - min(a, b, c, d) > 1000


a = [int(x) for x in open('17data/17-3.txt')]
c = []
for i in range(len(a) - 3):
    if f(a[i], a[i+1], a[i+2], a[i+3]):
        c.append(a[i] + a[i+1] + a[i+2] + a[i+3])
print(len(c), min(c))