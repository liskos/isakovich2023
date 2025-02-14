def f(x, y, z):
    return (x + 3, y, z), (x, y + 3, z), (x, y, z + 3), (x + 13, y, z), (x, y + 13, z), (x, y, z + 13),(x + 23, y, z), (x, y + 23, z), (x, y, z + 23)


a = [[' '] * 600 for _ in range(600)]

for i in range(600):
    for j in range(600):
        for d in range(600):
            if i + j + d >= 73:
                a[i][j][d] = '0'
for i in range(600):
    for j in range(600):
        for d in range(600):
            if a[i][j][d] == ' ' and any(a[x][y][z] == '0' for x, y, z in f(i, j, d)):
                a[i][j][d] = '1'
for i in range(600):
    for j in range(600):
        for d in range(600):
            if a[i][j][d] == ' ' and all(a[x][y][z] == '1' for x, y, z in f(i, j, d)):
                a[i][j][d] = '2'
for i in range(600):
    for j in range(600):
        for d in range(600):
            if a[i][j][d] == ' ' and any(a[x][y][z] == '2' for x, y, z in f(i, j, d)):
                a[i][j][d] = '3'
for i in range(600):
    for j in range(600):
        for d in range(600):
            if a[i][j][d] == ' ' and all(a[x][y][z] in '13' for x, y, z in f(i, j, d)):
                a[i][j][d] = '4'
import sys

sys.stdout = open('87.xls', mode='w')

for i in range(1, 600):
    print(*a[i][1:], sep='\t')