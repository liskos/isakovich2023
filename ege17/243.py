def f(a, b):
    return a > ma or b > ma


a = [int(x) for x in open('17data/17-243.txt')]
ma = max([x for x in a if x % 19 == 0])
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), min(c))