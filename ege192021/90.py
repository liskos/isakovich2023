def f(x, y):
    return (x + 1, y), (x, y + 1), (x * 3, y), (x, y * 3)


a = [[' '] * 600 for _ in range(600)]

for i in range(600):
    for j in range(600):
        if 79 >= i + j >= 60:
            a[i][j] = '0'
        elif i + j >= 79:
            a[i][j] = '-1'
for i in range(600):
    for j in range(600):
        if a[i][j] == ' ' and any(a[x][y] == '0' for x, y in f(i, j)):
            a[i][j] = '1'
for i in range(600):
    for j in range(600):
        if a[i][j] == ' ' and all(a[x][y] in '-1' for x, y in f(i, j)):
            a[i][j] = '2'
for i in range(600):
    for j in range(600):
        if a[i][j] == ' ' and any(a[x][y] == '2' for x, y in f(i, j)):
            a[i][j] = '3'
for i in range(600):
    for j in range(600):
        if a[i][j] == ' ' and all(a[x][y] in '-13' for x, y in f(i, j)):
            a[i][j] = '4'
import sys

sys.stdout = open('90.xls', mode='w')

for i in range(1, 600):
    print(*a[i][1:], sep='\t')