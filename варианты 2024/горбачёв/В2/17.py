a = [int(x) for x in open('17.txt')]


def f(a):
    if 1000 <= a <= 9999:
        return 1
    else:
        return 0


ot = [x for x in a if x < 0 and x % 5 == 0]
c= []
for i in range(len(a) - 2):
    if (f(a[i]) + f(a[i + 1]) + f(a[i + 2])) >= 2 and a[i] + a[i+1] + a[i+2] >= len(ot):
        c.append(a[i]+a[i+1]+a[i+2])

print(len(c), min(c))