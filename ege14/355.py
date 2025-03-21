

for x in range(13):
    r = int('80121', 13) + (x * 13 ** 3) - int('70575', 13) + (x * 13 ** 3)
    if r % 19 == 0:
        print(r // 19, x)