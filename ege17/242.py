def f(a, b, c):
    return (a < sr or b < sr or not(c < sr)) and (str(a).count('1') > 0 and str(b).count('1') > 0 and str(c).count('1') > 0)


a = [int(x) for x in open('17data/17-1.txt')]
sr = sum(a) // len(a)
c = []
for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))