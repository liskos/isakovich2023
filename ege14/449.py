for x in range(1, 16):
    r = int('3bb08', 16) + (x * 16 ** 1) + int('b67a0fe62', 16) + (x * 16 ** 4) + int('bea20d49b', 16) + (x * 16 * 4) + int('8d7d0', 16) + (x * 16 ** 0)
    if r % 15 == 0:
        print(r // 15, x)
