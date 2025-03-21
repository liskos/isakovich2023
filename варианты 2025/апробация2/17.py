a = [int(x) for x in open('17.txt')]

m = min(a)
c = []
for i in range(len(a) - 1):
    if a[i] % 16 == m or a[i+1] % 16 == m:
        c.append(a[i] + a[i+1])
print(len(c), max(c))