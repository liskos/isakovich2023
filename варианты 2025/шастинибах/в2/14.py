a = []
for x in range(24):
    s = int('120734', 24) + (x * 24 ** 3) + int('809503', 24) + (x * 24 ** 1) + (x * 24 ** 4) + int('240796', 24) + (x * 24 ** 3)
    if s % 23 == 0:
        a.append(s // 23)
print(max(a))