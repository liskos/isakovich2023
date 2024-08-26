a = [int(x) for x in open('17.txt')]
ami = min([x for x in a if x % 41 == 0 and x > 0])
c = []
for i in range(len(a) - 1):
    if a[i] != a[i+1] and abs(a[i] - a[i+1]) % ami == 0:
        c.append(a[i] + a[i+1])
print(len(c), max(c))
