for p in range(7, 36):
    for z in range(1, p):
        for x in range(1, p):
            for y in range(1, p):
                r = int('030', p) + (y * p ** 0) + (y * p ** 2) + int('065', p) + (y * p ** 2)
                s = int('0200', p) + (z * p ** 1) + (x * p ** 3)
                if r == s:
                    print(str(x) + str(y) + str(z), p)
                    print(x * p ** 2 + y * p ** 1 + z)