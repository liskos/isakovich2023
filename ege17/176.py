def f(a):
    return ((a % 10) + (a % 100 // 10)) > 15 and a % 3 > 0 and a % 4 > 0 and a % 7 > 0


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(min(c), sum(c))