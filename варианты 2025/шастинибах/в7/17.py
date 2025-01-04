def f(a):
    return int(str(a).count('0') > 0)

a = [int(x) for x in open('17.txt')]

m = max(a)
c = []
for i in range(len(a) - 2):
    if f(a[i]) + f(a[i+1]) + f(a[i+2]) <= 1 and a[i] + a[i+1] + a[i+2] < m / 2:
        c.append(a[i] + a[i+ 1] + a[i+2])
print(len(c), max(c))