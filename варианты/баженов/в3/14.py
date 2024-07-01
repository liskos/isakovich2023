a = []
for x in range(9):
    for y in range(1, 9):
        n = int("56001", 9) + x * 9 ** 2 + y * 9 ** 1 - int('00a02', 11) - y * 11 ** 4 - x * 11 ** 3
        if n % 6 == 0 and x + y == 7 and n > 0:
            print(n // 6)


