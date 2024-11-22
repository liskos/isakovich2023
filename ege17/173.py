def f(a):
    return a % 3 == 0 and a % 9 > 0 and a % 10 > 3


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), sum(c) // len(c))