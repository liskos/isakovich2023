

for x in range(1, 15):
    r = int('82019', 15) + (x * 15 ** 2) - (int('60073', 15) + (x * 15 ** 3))
    if r % 11 == 0:
        print(r // 11, x)