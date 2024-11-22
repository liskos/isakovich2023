def f(a):
    return a % 13 == 4 and a % 8 == 1


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(max(c), sum(c))