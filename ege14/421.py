for p in range(8, 37):
    for x in range(1, p):
        for y in range(1, p):
            r = int('71', p) * int('57', p)
            s = int('007', p) + (x * p ** 2) + (y * p ** 1)
            if r == s:
                print(int(str(y) + str(x), p), p)
                print(y * p + x)