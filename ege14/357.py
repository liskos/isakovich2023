

for x in range(15):
    for y in range(17):
        r = int('12305', 15) + (x * 15 ** 1) + int('6709', 17) + (y * 17 ** 1)
        if r % 131 == 0:
            print(r // 131, y)