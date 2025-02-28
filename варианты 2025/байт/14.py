for x in range(16, 21):
    for y in range(1, 21):
        r = int('13f10', x) + 1 + int('15050', 21) + x ** 2 + 1
        if r % 32 == 0:
            print(r//32)
