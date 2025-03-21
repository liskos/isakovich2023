z = False
for a in range(1, 10000):
    for x in range(13):
        for y in range(13):
            m = int('202305', 15) + (x * 15) + (y * 15 ** 4)
            n = int('67090', 13) + (y * 13 ** 0) + (x * 13 ** 2)
            if (m + a) % n == 0:
                print(a)
                z = True
                break
        if z:
            break
    if z:
        break