def f(a, b):
    return (a < sr or b < sr) and (str(a).count('7') > 0 or str(b).count('7') > 0)


a = [int(x) for x in open('17data/17-4.txt')]
sr = sum(a) // len(a)
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), min(c))