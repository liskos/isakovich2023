def f(a):
    return (a % 31 == 0 or a % 47 == 0 or a % 53 == 0) and (a % 3 == a % 5)


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), min(c))