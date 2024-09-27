c = []
a = [int(x) for x in open('17.txt')]
for i in range(len(a) - 1):
    if abs(a[i]) % 100 == 13 or abs(a[i+1]) % 100 == 13:
        c.append(a[i] + a[i+1])
print(len(c), max(c))


