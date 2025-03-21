

for x in range(19):
    r = int('55036', 19) + (x * 19 ** 2) + int('02724', 19) + (x * 19 ** 4)
    if r % 11 == 0:
        print(r // 11, x)