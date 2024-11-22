def f(a):
    return a % 3 == 0 and a % 7 > 0 and a % 17 > 0 and a % 19 > 0 and a % 27 > 0


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), max(c))