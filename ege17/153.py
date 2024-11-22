def f(a, b):
    return a < b


a = [int(x) for x in open('17data/17-1.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(abs(a[i]) - abs(a[i+1]))
print(len(c), min(c))