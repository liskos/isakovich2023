for p in range(10, 37):
    for x in range(1, p):
        for y in range(1, p):
            r = int('71', p) * int('69', p)
            s = int('009', p) + (x * p ** 2) + (y * p ** 1)
            if r == s:
                print(int(str(y) + str(x), p), p)
                print(y * p + x)