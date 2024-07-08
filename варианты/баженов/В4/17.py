c = []
a = [int(x) for x in open('17.txt')]
b = max([x for x in a if 10 <= x <= 99])
for i in range(len(a) - 1):
    if (a[i] % 10 == 4 or not(a[i+1] % 10 == 4)) <= b:
        c.append(a[i] + a[i+1])
print(len(c), max(c))
