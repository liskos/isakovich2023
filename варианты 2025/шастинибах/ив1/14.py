for x in range(17):
    r = int('4b301c7', 14) + x * 14 ** 3 + int('50g83f7', 17) + x * 17 ** 5
    if r % 15 == 0:
        print(x, r // 15)