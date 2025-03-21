

for x in range(1, 22):
    for y in range(13):
        r = int('02305', 22) + (x * 22 ** 1) + (x * 22 ** 4) - int('67090', 13) + (y * 13 ** 0) + (y * 13 ** 2)
        if r % 57 == 0:
            print(r // 57, x + y)