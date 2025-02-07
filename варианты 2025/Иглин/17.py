a = [int(x) for x in open('17.txt')]

m = abs(min([x for x in a if abs(x) % 12 == 0]))

c = []
for i in range(len(a) - 2):
    if (abs(a[i]) > 9999 or abs(a[i+1]) > 9999 or abs(a[i+2]) > 9999) and abs(a[i] * a[i+1] * a[i+2] % 100) == m:
        c.append(abs(a[i] + a[i+1] + a[i+2]))
print(len(c), min(c))