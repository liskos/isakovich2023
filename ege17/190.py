

a = [int(x) for x in open('17data/17-7.txt')]
c = []
for i in range(len(a)):
    if a[i] % 8 == 7 and a[i] // 8 % 8 != 2:
        c.append(a[i])
print(len(c), max(c))