def f(a, b, c):
    return (a < sr or b < sr or c < sr) and (str(a).count('2') > 0 or str(b).count('2') > 0 or not(str(c).count('2') > 0))


a = [int(x) for x in open('17data/17-1.txt')]
sr = sum(a) // len(a)
c = []
for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))