a = [int(x) for x in open('17.txt')]
ma = min([x for x in a])
c = []
for i in range(len(a) - 1):
    if a[i] % 16 == ma or a[i+1] % 16 == ma:
        c.append(a[i] + a[i+1])
print(len(c), max(c))