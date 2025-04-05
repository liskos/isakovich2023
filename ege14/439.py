
a = []
for x in range(1, 15):
        r = int('67845065', 15) + (x * 15 ** 2) + int('1023456', 15) + (x * 15 ** 5)
        if r % 14 == 0:
            a.append(x)
            print(r// 14, x)
