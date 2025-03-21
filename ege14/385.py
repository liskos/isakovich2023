

for x in range(16):
    r = int('100a', 16) + (x * 16 ** 1) + int('ff078', 16) + (x * 16 ** 2)
    if r % 19 == 0:
        print(r // 19, x)
