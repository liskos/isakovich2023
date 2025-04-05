for p in range(9, 37):
    for x in range(1, p):
        for y in range(1, p):
            r = int('75', p) * int('87', p)
            s = int('1002', p) + (x * p ** 2) + (y * p ** 1)
            if r == s:
                print(int(str(y) + str(x), p), p)
                print(y * p + x)