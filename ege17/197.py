def f(a, b):
    return 999 >= a + b >= 100 and (a + b) % 10 > (a + b) // 10 % 10

a = [int(x) for x in open('17data/17-10.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), min(c))