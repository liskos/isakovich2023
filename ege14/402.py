for p in range(8, 36):
    for x in range(1, p):
        for y in range(1, p):
            r = int('1077', p) + (x * p ** 2) + int('0077', p) + (x * p ** 2) + (x * p ** 3)
            s = int('0000', p) + (y * p ** 0) + (y * p ** 1) + (y * p ** 3)
            if r == s:
                print(str(y) + str(x) + str(y) + str(x), p)
                print(y * p ** 3 + x * p ** 2 + y * p + x)
