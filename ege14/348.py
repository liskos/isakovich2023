

for x in range(18):
    r = int('90090', 18) + (x * 18 ** 0) + int('22570', 18) + (x * 18 ** 0)
    if r % 15 == 0:
        print(r // 15, x)