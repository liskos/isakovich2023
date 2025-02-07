def f(x, y):
    return (x - 1, y), (x, y - 1), ((x +1)// 2, y), (x, (y+1) // 2)


a = [[' '] * 400 for _ in range(400)]

for i in range(400):
    for j in range(400):
        if i + j <= 20:
            a[i][j] = '0'
for i in range(400):
    for j in range(400):
        if a[i][j] == ' ' and any(a[x][y] == '0' for x, y in f(i, j)):
            a[i][j] = '1'
for i in range(400):
    for j in range(400):
        if a[i][j] == ' ' and all(a[x][y] == '1' for x, y in f(i, j)):
            a[i][j] = '2'
for i in range(400):
    for j in range(400):
        if a[i][j] == ' ' and any(a[x][y] == '2' for x, y in f(i, j)):
            a[i][j] = '3'
for i in range(400):
    for j in range(400):
        if a[i][j] == ' ' and all(a[x][y] in '13' for x, y in f(i, j)):
            a[i][j] = '4'
import sys

sys.stdout = open('49.xls', mode='w')

for i in range(1, 400):
    print(*a[i][1:], sep='\t')