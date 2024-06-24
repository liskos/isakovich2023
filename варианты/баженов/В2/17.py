a = [int(x) for x in open('17.txt')]
b = []
m613 = max([x for x in a if x % 613 == 0])
for i in range(len(a) - 2):
    z = a[i:i+3]
    k = [x for x in z if str(x)[0] == '7']
    if len(k) <= 2 and sum(z) > m613:
        b.append(z[0] * z[1] * z[2])
print(len(b), max(b))


