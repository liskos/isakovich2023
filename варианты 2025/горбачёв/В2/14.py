for x in range(1, 1222):
    k = 0
    s = 4 ** x - 3 ** 331 + 9 ** 17
    while s > 0:
        if s % 5 == 0:
            k += 1
        s = s // 5
    if k == 77:
        print(x)
