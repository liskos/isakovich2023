

for x in range(17):
    r = int('13101', 15) + (x * 15 ** 1) + int('1303', 17) + (x * 17 ** 1)
    if r % 11 == 0:
        print(r // 11, x)