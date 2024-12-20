c = []
for x in range(1, 25):
    r = int('A407F2', 25) + (x * 25 ** 3) + int('N0G50H', 25) + (x * 25 ** 1) + (x * 25 ** 4) + int('740M26', 25) + (x * 25 ** 3)
    if r % 24 == 0:
        c.append(r // 24)
print(max(c))