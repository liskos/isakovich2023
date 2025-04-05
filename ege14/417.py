for p in range(6, 37):
    for x in range(1, p):
        for y in range(1, p):
            r = int('23', p) * int('45', p)
            s = int('003', p) + (x * p ** 2) + (y * p ** 1)
            if r == s:
                print(int(str(y) + str(x), p), p)
                print(y * p + x)