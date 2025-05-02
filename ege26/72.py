def f(filename):
    file = open(filename)
    n, m, k = map(int, file.readline().split())
    a = [[0] * (n + 1) for _ in range(m + 1)]
    print(f'{n} - размер по горизонтали')
    print(f'{m} - размер по вертикали')
    print(f'{k} - занятых клеток')
    for _ in range(k):
        row, column = map(int, file.readline().split())
        a[row][column] = 1
    # for i in range(1, m + 1):
    #     print(a[i][1:])
    rez = [0] * (m + 1)
    for row in range(1, m + 1):
        for i in range(1, n - 2):
            if a[row][i] == 0 and a[row][i+1] == 0 and a[row][i+2] == 0 and a[row][i+3] == 0:
                rez[row] += 1
    return sum(rez), rez.index(max(rez))


print(f('26data/26-72.txt'))