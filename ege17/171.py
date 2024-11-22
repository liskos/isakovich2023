def f(a):
    return a % 31 == 0 and a % 47 == 0 and a % 53 == 0


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), min(c))