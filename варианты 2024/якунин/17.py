a = [int(x) for x in open('17.txt')]

c = []
ma = (max([x for x in a if x % 100 == 14]))
for i in range(len(a) - 2):
    if a[i] % 14 == 0 and a[i+1] % 14 == 0 and a[i+2] % 14 == 0 and a[i] + a[i+1] + a[i+2] > ma * 2:
        c.append(a[i]+a[i+1]+a[i+2])
print(len(c), min(c))
