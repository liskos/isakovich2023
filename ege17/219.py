def f(a, b):
    return (a < sr and b < sr) and (a % 10 == 9 or b % 10 == 9)


a = [int(x) for x in open('17data/17-4.txt')]
sr = sum(a) // len(a)
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), max(c))