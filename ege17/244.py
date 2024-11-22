def f(a, b):
    return a < ma and b < ma


a = [int(x) for x in open('17data/17-243.txt')]
ma = max([x for x in a if x % 119 == 0])
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), max(c))