for p in range(10, 36):
    for x in range(1, p):
        for y in range(1, p):
            r = int('3405', p) + (x * p ** 1) + int('0903', p) + (x * p ** 1) + (x * p ** 3)
            s = int('0068', p) + (y * p ** 2) + (y * p ** 3)
            if r == s:
                print(str(y) + str(x) + str(x) + str(y), p)
                print(y * p ** 3 + x * p ** 2 + x * p + y)