def f(a):
    return (a % 10 == 2 or a % 10 == 7) and a % 3 == 0 and a % 11 == 0


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), min(c))