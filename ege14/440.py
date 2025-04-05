
a = []
for x in range(17):
        r = int('12346017', 17) + (x * 17 ** 2) + int('70171', 17) + (x * 17 ** 3)
        if r % 16 == 0:
            a.append(x)
            print(r// 16, x)
