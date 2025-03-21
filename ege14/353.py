

for x in range(1, 17):
    r = int('66063', 17) + (x * 17 ** 2) - (int('50810', 17) + (x * 17 ** 3))
    if r % 11 == 0:
        print(r // 11, x)