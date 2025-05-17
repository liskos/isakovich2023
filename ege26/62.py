def f(filename):
    file = open(filename)
    n, m = map(int, file.readline().split())
    a = [list(file.readline().split()) for _ in range(n)]
    a = sorted(a)
    print(a)
    v = []
    c = []
    for x in a:
        if int(x[0]) <= sum(v) and x[1] == 'Q':
            v.append(int(x[0]))
            c.append(x[1])
        elif int(x[0]) <= sum(v) and x[1] == 'Z':
            v.append(int(x[0]))
            c.append(x[1])
        else:
            break
    print(v)



print(f('62.txt'))