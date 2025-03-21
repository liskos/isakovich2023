

for x in range(17):
    r = int('97590', 17) + (x * 17 ** 0) + int('30108', 17) + (x * 17 ** 3)
    if r % 11 == 0:
        print(r // 11, x)