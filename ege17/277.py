def f(a):
    n = []
    while a > 0:
        n.append(n % 3)
        n = n // 3
    return n

a = [int(x) for x in open('17data/17-277.txt')]
ma = f([x for x in a])

c = []
for i in range(len(a) - 1):
    if :
        c.append(a[i] + a[i+1])
print(len(c), max(c))