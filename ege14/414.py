for p in range(9, 100):
    for z in range(0, p):
        for x in range(0, p):
            for y in range(0, p):
                r =  y + 10*p + 7 + 2 * y * p ** 2
                s = p**3 + (x * p ** 2) + z * (p+1)
                if r == s:
                    print(x, y, z, p)
                    print(x * p ** 2 + y * p ** 1 + z)