for x in range(16, 21):
    for y in range(0, 21):
        r = int('13f10', x) + y + int('15050', 21) + x *21** 2 + y
        if r % 32 == 0:
            print(r, r//32)
