a = [int(x) for x in open('17.txt')]
m = min([x for x in a])
def f(a):
    if a > 0:
        return 1
c = []
for i in range(len(a) - 2):
    t = f(a[i]) + f(a[i+1]) + f(a[i+2])
    if t <= 1 and (a[i] + a[i+1] + a[i+2]) % 10 == m % 10:
        c.append(abs(a[i] + a[i+1] + a[i+2]))
print(len(c), max(c))