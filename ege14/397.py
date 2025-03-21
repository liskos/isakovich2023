

for p in range(10, 36):
    for x in range(1, 100):
        for y in range(100):
            r = int('3970', p) + (x * p ** 0) + int('0904', p) + (x * p ** 1) + (x * p ** 3)
            s = int('0190', p) + (y * p ** 0) + (y * p ** 3)
            if r == s:
                print(int(str(y) + str(y) + str(x) + str(x), p))

