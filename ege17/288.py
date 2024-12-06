def f(d):
    n = []
    while d > 0:
        n.append(d % 7)
        d = d // 7
    return n[::-1]

a = [int(x) for x in open('17data/17-288.txt')]


c = []
for i in range(len(a) - 2):
    if f(a[i])[-1] != f(a[i+1])[-1] != f(a[i+2])[-1] and (a[i] < 0 or a[i+1] < 0 or a[i+2] < 0):
        c.append(max(a[i], a[i+1], a[i+2]) - min(a[i], a[i+1], a[i+2]))
print(len(c), min(c))