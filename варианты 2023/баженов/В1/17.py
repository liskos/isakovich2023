a = [int(x) for x in open('17.txt')]
m = 10000
k = 0
for i in range(len(a) - 2):
    if (sum(map(int, str(a[i]))) % 2 == 1 and (sum(map(int, str(a[i + 1]))) % 2 == 1) and
            (sum(map(int, str(a[i + 2]))) % 2 == 1) and ((a[i] % 6 == 3) or (a[i + 1] % 6 == 3) or (a[i + 2] % 6 == 3))):
        if a[i] < m:
            m = a[i]
        if a[i + 1] < m:
            m = a[i + 1]
        if a[i + 2] < m:
            m = a[i + 2]
        k += 1
print(k)
print(m)
