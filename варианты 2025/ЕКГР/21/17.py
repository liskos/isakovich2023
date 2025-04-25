a = [int(x) for x in open('17.txt')]
def f(x):
    return 100000 > abs(x) >= 10000 and abs(x) % 100 == 43

ma = max([x for x in a if 100000 > abs(x) >= 10000 and abs(x) % 100 == 43])
c = []

for i in range(len(a) - 2):
    if (f(a[i]) or f(a[i+1]) or f(a[i+2])) and (a[i] ** 2) + (a[i+1] ** 2) + (a[i+2] ** 2) <= ma ** 2:
        c.append(a[i] ** 2 + a[i+1] ** 2 + a[i+2] ** 2)
print(len(c), min(c))