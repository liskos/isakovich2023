c = []
for x in range(25):
    r = int('11353012', 25) + (x * 25 ** 2) + int('135021', 25) + (x * 25 ** 2)
    if r % 24 == 0:
        c.append(r//24)
print(c)