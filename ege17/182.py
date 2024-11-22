def f(a):
    return a % 13 == 7 and a % 7 > 0 and a % 11 > 0


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(max(c) - min(c), len(c))