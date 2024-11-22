def f(a):
    return str(a)[-1] in '02468' and


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), max(c) - min(c))