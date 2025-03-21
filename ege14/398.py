

for p in range(10, 36):
    for x in range(1, 100):
        for y in range(100):
            r = int('5083', p) + (x * p ** 2) + int('0909', p) + (x * p ** 1) + (x * p ** 3)
            s = int('0200', p) + (y * p ** 0) + (y * p ** 3)
            if r == s:
                print(int(str(x) + str(y) + str(y) + str(x), p))

