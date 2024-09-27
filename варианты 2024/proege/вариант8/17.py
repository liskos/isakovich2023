def f(n):
    if 1000 <= abs(n) < 10000 and n % 2 == 0:
        return 1
    else:
        return 0


c = []
a = [int(x) for x in open('17.txt')]
m3 = max([x for x in a if x % 9 == 3])
for i in range(len(a) - 2):
    if f(a[i]) + f(a[i+1]) + f(a[i+2]) <= 1 and a[i+1] + a[i+2] + a[i] <= m3:
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))
