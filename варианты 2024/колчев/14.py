a = set()

for x in range(1, 25):
    r = int('8AF7011', 25) + (x * 25 ** 2) + int('0DA87', 25) + (x * 25 ** 4)
    for y in range(1, 101):
        if r % y == 0:
            a.add(y)
print(len(a))
