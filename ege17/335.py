
a = [int(x) for x in open('17data/17-335.txt')]
sr = min([x for x in a if x % 43 == 0])
c = []
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) % sr == 0 or a[i] % 10 == sr % 10 or a[i+1] % 10 == sr % 10:
        c.append(a[i+1])
        c.append(a[i])
print(len(c)//2, max(c))