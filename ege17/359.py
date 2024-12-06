
a = [int(x) for x in open('17data/17-354.txt')]
m = min([x for x in a if x % 10 == 2])
s = max([x for x in a if x % 10 == 9])
c = []
for i in range(len(a) - 1):
    if (a[i] % 10 == ((a[i+1] % 10) + 1) or (a[i] % 10 == (a[i+1] % 10) - 1)) and a[i] % 5 == 0 and not(a[i+1] % 5 == 0) and a[i] ** 2 + a[i+1] ** 2 >= m ** 2 and a[i] + a[i+1] > 0:
        c.append(a[i] + a[i+1])
print(len(c), min(c))