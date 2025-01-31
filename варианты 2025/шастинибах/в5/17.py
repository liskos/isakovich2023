a = [int(x) for x in open('17.txt')]

m = min([x for x in a if abs(x) % 10 == 7])
c = []
for i in range(len(a) - 2):
    if (abs(a[i]) >= 10000 or abs(a[i+1]) >= 10000 or abs(a[i+2]) >= 10000) and abs(a[i]*a[i+1]*a[i+2]) % m == 0:
        c.append(a[i] * a[i+1] * a[i+2])
print(len(c), max(c))