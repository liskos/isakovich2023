def f(a, b):
    return (a < sr or b < sr) and ((a % 7 == 0 and a % 3 > 0 and a % 11 > 0 and a % 13 > 0) or (b % 7 == 0 and b % 3 > 0 and b % 11 > 0 and b % 13 > 0))


a = [int(x) for x in open('17data/17-4.txt')]
sr = sum(a) // len(a)
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), min(c))