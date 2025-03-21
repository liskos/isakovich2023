

for p in range(10, 36):
    for x in range(1, 100):
        for y in range(100):
            r = int('8900', p) + (x * p ** 1) + int('0604', p) + (x * p ** 1) + (x * p ** 3)
            s = int('10014', p) + (y * p ** 2) + (y * p ** 3)
            if r == s:
                print(int(str(y) + str(x) + str(y) + str(x), p))

