def f(a):
    return hex(a)[-1] == 'b' and a % 7 == 0 and a % 6 != 0 and a % 13 != 0 and a % 19 != 0


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(sum(c), len(c))