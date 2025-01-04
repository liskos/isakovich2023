def f(filename):
    file = open(filename)
    n, s = map(int, file.readline().split())
    print(n, s)
    l = []
    with file:
        for line in file:
            id, t, k = map(int, line.split())
            l.append([id, t, k])
    print(l)

if __name__ == '__main__':
    print(f('26.txt'))