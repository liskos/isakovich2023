c = []
a = [int(x) for x in open('17.txt')]
for i in range(len(a) - 3):
    if (abs(a[i]) % 100 == 13) != (abs(a[i+3]) % 100 == 13):
        c.append(a[i] + a[i+3])
print(len(c), max(c))


