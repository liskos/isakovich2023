

a = [int(x) for x in open('17data/17-296.txt')]
def f():
    for i in a:
        while a[i] > 9:
            a[i] = a[i] // 10


c = []
for i in range(len(a) - 1):
    if a[i] * a[i+1] >:
        c.append(a[i] + a[i+1])
print(len(c), max(c))