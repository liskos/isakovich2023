for p in range(9, 37):
    for z in range(1, p):
        for x in range(1, p):
            for y in range(1, p):
                r = int('020', p) + (y * p ** 0) + (y * p ** 2) + int('057', p) + (y * p ** 2)
                s = int('0003', p) + (x * p ** 3) + (z * p ** 1) + (x * p ** 2)
                if r == s:
                    print(str(x) + str(y) + str(z), p)
                    print(x * p ** 2 + y * p ** 1 + z)