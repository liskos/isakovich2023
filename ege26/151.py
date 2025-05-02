def f(filename):
    file = open(filename)
    n, k = map(int, file.readline().split())
    print(f'{n} - кандидаты')
    print(f'{k} - кол-во мест')
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    a = [i+[i[1]+i[2]+i[3]] for i in a]
    a.sort(key=lambda x:(x[5], x[4], -x[0]), reverse=True)
    for i in range(n):
        print(a[i], a[i][5])
    otob = a[:k]
    print(otob)
    pos_ball = otob[-1][5]
    print("последний балл", pos_ball)
    print([i for i in a if i[5]==155][-1])
print(f('26data/26-151.txt'))