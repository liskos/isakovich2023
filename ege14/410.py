for p in range(14, 100):
    for q in range(14, 100):
        r = 10 * p ** 2 + 11 * p + 12
        r2 = 11 * q ** 2 + 12 * q + 13
        if r == r2:
            print(p, q, r)