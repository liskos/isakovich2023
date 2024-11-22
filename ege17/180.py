def f(a):
    return a % 5 == 3 and a % 9 == 5 and a % 8 != 7


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), max(c))