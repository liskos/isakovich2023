a = [int(x) for x in open('17.txt')]
rez = []
for i in range(len(a) - 2):
    z = a[i:i+3]
    zz = [x for x in z if sum(map(int, str(x))) % 2 == 1]
    zzz = [x for x in z if x % 6 == 3]
    if len(zz) == 3 and len(zzz) >= 1:
        rez.extend(z)
print(len(rez) // 3, min(rez))