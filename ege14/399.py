

for p in range(10, 36):
    for x in range(1, 100):
        for y in range(1, 100):
            r = int('8706', p) + (x * p ** 1) + int('0508', p) + (x * p ** 1) + (x * p ** 3)
            s = int('07092', p) + (y * p ** 2) + (y * p ** 4)
            if r == s:
                print(int(str(y) + str(x) + str(x) + str(y), p))

