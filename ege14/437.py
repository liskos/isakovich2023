

for x in range(23):
        r = int('7038596', 23) + (x * 23 ** 5) + int('14036', 23) + (x * 23 ** 2) + int('6107', 23) + (x * 23 ** 1)
        if r % 22 == 0:
            print(r // 22, x)
