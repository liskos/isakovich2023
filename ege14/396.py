

for p in range(10, 36):
    for x in range(1, 100):
        for y in range(100):
            r = int('4909', p) + (x * p ** 1) + int('0600', p) + (x * p ** 1) + (x * p ** 3)
            s = int('0009', p) + (y * p ** 1) + (y * p ** 3)
            if r == s:
                print(int(str(y) + str(y) + str(x) + str(x), p))

