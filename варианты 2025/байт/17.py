a = [int(x) for x in open('17.txt')]

m = max([x for x in a if len(str(abs(x))) == 5 and abs(x) % 100 == 42])


c = []
for i in range(len(a) - 1):
    if ((abs(a[i]) % 100 == 42 and len(str(abs(a[i]))) == 5) and not(abs(a[i+1]) % 100 == 42 and len(str(abs(a[i+1]))) == 5)) and a[i] ** 2 + a[i+1] ** 2 >= m:
        c.append(a[i] + a[i+1])

print(len(c) * 2, max(c))