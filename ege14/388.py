
a = []
for x in range(8):
    for y in range(8):
        for y2 in range(8):
            r = int('36053', 8) + (x * 8 ** 2) - (int('4003', 8) + (y * 8 ** 1) + y2*8**2)
            if r > 0:
                a.append(r)
print(min(a))
