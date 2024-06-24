for x in range(36):
    s = int("i0", 36) + x + int('l0ve', 36) + x * 36 ** 2 + int('anime', 36)
    if s % 25 == 0:
        print(s // 25)