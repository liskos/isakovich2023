for p in range(10, 36):
    for x in range(1, p):
        for y in range(1, p):
            r = int('4046', p) + (x * p ** 2) + int('0017', p) + (x * p ** 2) + (x * p ** 3)
            s = int('03860', p) + (y * p ** 0) + (y * p ** 4)
            if r == s:
                print(str(x) + str(y) + str(x) + str(y), p)
                print(x * p ** 3 + y * p ** 2 + x * p + y)
