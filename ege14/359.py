

for x in range(25):
    for y in range(25):
        r = int('702305', 25) + (x * 25 ** 1) + (y * 25 ** 4) + int('67090', 11) + (y * 11 ** 0) + (x * 11 ** 2)
        if r % 131 == 0:
            print(r // 131, x, y)