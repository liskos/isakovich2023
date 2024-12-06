

a = [int(x) for x in open('17data/17-273.txt')]
ma = max([x for x in a])

c = []
for i in range(len(a) - 2):
    if a[i] + a[i+1] + a[i+2] < ma:
        c.append(a[i])
        c.append(a[i+1])
        c.append(a[i+2])
print(len(c)//3, max(c) + min(c))