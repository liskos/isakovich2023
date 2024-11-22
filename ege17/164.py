def f(a, b, c):
    return (a % 3 == 0 and b % 3 == 0 and c % 3 == 0) and (a % 12 == 0 or b % 12 == 0 or c % 12 == 0)


a = [int(x) for x in open('17data/17-3.txt')]
c = []
for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))