

for x in range(8):
    for y in range(8):
        r = int('36053', 8) + (x * 8 ** 2) - int('403', 8) + (y * 8 ** 1)
        if r > 0:
            print(r, x, y)
