

for x in range(16):
    r = int('85690', 16) + (x * 16 ** 0) + int('12048', 16) + (x * 16 ** 2)
    if oct(r)[2:].count('0') + oct(r)[2:].count('2') + oct(r)[2:].count('4') + oct(r)[2:].count('6') <= 2:
        print(oct(r)[2:], x)
