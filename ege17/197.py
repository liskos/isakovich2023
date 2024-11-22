def f(a, b, c):
    return a + b + c >= 100 and (a + b + c) % 10 > (a + b + c) // 10 % 10

a = [int(x) for x in open('17data/17-10.txt')]
c = []
for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), min(c))