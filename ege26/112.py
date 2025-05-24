def f(file_name):
    file = open(file_name)
    n, k = map(int, file.readline().split())
    a = [list(map(int, file.readline().split())) for _ in range(n)]
    print(len(set([x[1] for x in a])))
    a.sort(key=lambda x: (x[0], x[1]))
    print(a)
    kamera = [0] * k
    print(kamera)
    nerazmest = []
    poslednya = 0
    for t_begin, t_end in a:
        for i in range(k):
            if kamera[i] <= t_begin:
                kamera[i] = t_end +1
                poslednya = i
                break
        else:
            nerazmest.append((t_begin, t_end))
    print(nerazmest)
    return n - len(nerazmest), poslednya + 1

print(*f('26data/26-112.txt'))
print("------------------------")
print(*f('112.txt'))