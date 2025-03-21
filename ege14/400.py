

for p in range(10, 36):
    for x in range(1, 100):
        for y in range(100):
            r = int('5016', p) + (x * p ** 2) + int('0005', p) + (x * p ** 1) + (x * p ** 2) + (x * p ** 3)
            s = int('11500', p) + (y * p ** 0) + (y * p ** 1)
            if r == s:
                print(int(str(y) + str(x) + str(y), p))

