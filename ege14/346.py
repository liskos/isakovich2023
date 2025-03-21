

for x in range(15):
    r = int('12305', 15) + (x * 15 ** 1) + int('10233', 15) + (x * 15 ** 3)
    if r % 14 == 0:
        print(r // 14, x)