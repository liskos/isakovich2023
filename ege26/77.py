def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    a = sorted(a)
    print(a)



print(f('77.txt'))