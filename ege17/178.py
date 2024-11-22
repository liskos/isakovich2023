def f(a):
    k = 0
    for i in [2, 3, 5, 7]:
        if a % i == 0:
            k += 1
    return k == 2


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), max(c) + min(c))