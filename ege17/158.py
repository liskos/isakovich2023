
a = [int(x) for x in open('17data/17-1.txt')]
c = []

ma = max(a)
for i in range(len(a)):
    while a[i] > a[i+1]:
        c.append(a[i])
print(len(c), min(c))