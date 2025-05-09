def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    a = sorted(a)
    print(f'{n} чисел')
    print(a)
    sr = sum(a) / len(a)
    med = a[n //2]
    print(sr, med)
    k = 0
    for x in a:
        if min(sr, med) <= x <= max(sr, med):
            k += 1
    return k






print(f('27test.txt'))
print(f('26data/26-J2.txt'))