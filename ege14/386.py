

for x in range(17):
    r = int('1000', 17) + (x * 17 ** 1) + int('F00FF', 17) + (x * 17 ** 2)
    if r % 13 == 0:
        print(r // 13, x)
