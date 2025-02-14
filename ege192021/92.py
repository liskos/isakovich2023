def f(x, y):
    return (x + 1, y), (x, y + 1), (x * 2, y), (x, y * 2)


a = [[' '] * 600 for _ in range(600)]

for i in range(600):
    for j in range(600):
        if 91 >= i + j >= 110:
            a[i][j] = '0'
        elif i + j >= 91:
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

sys.stdout = open('92.xls', mode='w')

for i in range(1, 600):
    print(*a[i][1:], sep='\t')