a = [int(x) for x in open('17.txt')]
am = min([x for x in a])
c = []
for i in range(len(a) - 2):
    if a[i] % 77 + a[i+1] % 77 == am:
        c.append(a[i] + a[i+1])
print(len(c), max(c))