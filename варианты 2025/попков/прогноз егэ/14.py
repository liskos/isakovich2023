

for x in range(21):
    r = int('05b08', 21) + x * 21 + x * 21 ** 4 + int('h05307', 21) + x * 21
    if r % 12 == 0:
        print(r // 12, x)