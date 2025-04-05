a = []

for x in range(1, 17):
    for y in range(1, 17):
        r = int('27a023', 16) + (x * 16 ** 2) + int('80e5d2', 16) + (y * 16 ** 4)
        if r % 5 == 0:
            a.append(x + y)
print(max(a))