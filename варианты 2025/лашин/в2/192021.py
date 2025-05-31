def f(x, y):
    return (x - 2, y), (x, y - 2), (x - 6, y), (x, y - 6), (x // 3, y), (x, y // 3)


a = [[' '] * 700 for _ in range(700)]

for i in range(700):
    for j in range(700):
        if i + j <= 64:
            a[i][j] = '0'
for i in range(700):
    for j in range(700):
        if a[i][j] == ' ' and any(a[x][y] == '0' for x, y in f(i, j)):
            a[i][j] = '1'
for i in range(700):
    for j in range(700):
        if a[i][j] == ' ' and all(a[x][y] == '1' for x, y in f(i, j)):
            a[i][j] = '2'
for i in range(700):
    for j in range(700):
        if a[i][j] == ' ' and any(a[x][y] == '2' for x, y in f(i, j)):
            a[i][j] = '3'
for i in range(700):
    for j in range(700):
        if a[i][j] == ' ' and all(a[x][y] in '13' for x, y in f(i, j)):
            a[i][j] = '4'
import sys

sys.stdout = open('192021.xls', mode='w')

for i in range(1, 700):
    print(*a[i][1:], sep='\t')