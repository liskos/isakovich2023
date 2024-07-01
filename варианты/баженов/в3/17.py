c = []
a = [int(x) for x in open('17.txt')]
b = max([x for x in a if abs(x) % 100 == 14])
for i in range(len(a) - 1):
    if (a[i] % 2 == a[i+1] % 2) != (max(a[i], a[i+1]) > b):
        c.append(a[i] + a[i+1])
print(len(c), max(c))
