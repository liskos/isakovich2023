def f(a, b, c):
    return (a < sr or b < sr or c < sr) and (a % 10 == 4 or b % 10 == 4 or not(c % 10 == 4))


a = [int(x) for x in open('17data/17-1.txt')]
sr = sum(a) // len(a)
c = []
for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))