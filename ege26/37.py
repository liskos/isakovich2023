def f(filename):
    file = open(filename)
    n, k = map(int, file.readline().split())
    v = [file.readline().split() for _ in range(n)]
    print(v)


print(f('37.txt'))