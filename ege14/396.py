

for p in range(10, 36):
    for x in range(1, p):
        for y in range(1, p):
            r = int('4909', p) + (x * p ** 1) + int('0600', p) + (x * p ** 1) + (x * p ** 3)
            s = int('0009', p) + (y * p ** 1) + (y * p ** 3)
            if r == s:
                print(str(y) + str(y) + str(x) + str(x), p)
                print(y*p**3 + y* p**2 + x*p + x)

