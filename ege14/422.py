for p in range(10, 37):
    for x in range(1, p):
        for y in range(1, p):
            r = int('93', p) * int('85', p)
            s = int('1000', p) + (x * p ** 2) + (y * p ** 0)
            if r == s:
                print(int(str(y) + str(x), p), p)
                print(y * p + x)