def f(x, y):
    return (x + 1, y), (x, y + 1), (x * 2, y), (x, y * 2), (x + 2, y), (x, y + 2), (x + 3, y), (x, y + 3), (x + 4, y), (x, y + 4), (x + 5, y), (x, y + 5)


a = [[' '] * 2000 for _ in range(2000)]

for i in range(2000):
    for j in range(2000):
        if i + j >= 610:
            a[i][j] = '0'
for i in range(2000):
    for j in range(2000):
        if a[i][j] == ' ' and any(a[x][y] == '0' for x, y in f(i, j)):
            a[i][j] = '1'
for i in range(2000):
    for j in range(2000):
        if a[i][j] == ' ' and all(a[x][y] == '1' for x, y in f(i, j)):
            a[i][j] = '2'
for i in range(2000):
    for j in range(2000):
        if a[i][j] == ' ' and any(a[x][y] == '2' for x, y in f(i, j)):
            a[i][j] = '3'
for i in range(2000):
    for j in range(2000):
        if a[i][j] == ' ' and all(a[x][y] in '13' for x, y in f(i, j)):
            a[i][j] = '4'
import sys

sys.stdout = open('192021.xls', mode='w')

for i in range(1, 2000):
    print(*a[i][1:], sep='\t')